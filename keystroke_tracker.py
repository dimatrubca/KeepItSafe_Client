import datetime
import logging
import random
from cryptography.fernet import Fernet
from pynput import keyboard
from dotenv import load_dotenv
from os.path import join, dirname
import time
import os
import threading
import numpy as np

from database.db import engine
from database import db
from database.models import Keystroke as KeyStrokeModel
from security import encrypt, decrypt
from sqlalchemy import and_
import keystroke_model

logger = logging.getLogger(__name__)

time_pressed = {}

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
cypher_suite = Fernet(os.environ['key'])


def on_press(key, user_id):
    print(type(key))
  #  print(key.char)
    if hasattr(key, 'char'):
        print('has char...')
        print(key)
        key=key.char
    else:
        print('NO CHAR:::')
        print(key)
        key = ' '
    
    print('char:', key)
   # key = key[1:-1]
    if time_pressed.get(key, None) is None:
        print(key)

        time_pressed[key] = datetime.datetime.now()


def on_release(key, user_id, signal):
    if hasattr(key, 'char'):
        key = key.char
    else:
        key = ' '

    try:
        press_timestamp = time_pressed[key]
    except Exception as e:
        print(e)
        return

    release_timestamp = datetime.datetime.now()

    if not press_timestamp:
        return

    print('char on release:', key)
    encrypted_key = encrypt(key)

    keystroke = KeyStrokeModel(pressed_timestamp=press_timestamp, released_timestamp=release_timestamp, key=encrypted_key, user_id=user_id)
    db.session.add(keystroke)
    db.session.commit()
    
    print(press_timestamp, release_timestamp, str(key))

    time_elapsed = datetime.datetime.now() - time_pressed[key]
    time_pressed[key] = None

    print(f"{key} was held for {time_elapsed} seconds")


#to do: check model fields
def validate_user(user_id, signal):
    thread =  threading.Timer(15, lambda: validate_user(user_id, signal))
    thread.daemon = True
    thread.start()

    min_time = datetime.datetime.now() - datetime.timedelta(seconds=20)

    keystrokes = db.session.query(KeyStrokeModel).filter(
        and_(
            KeyStrokeModel.user_id == user_id,
            KeyStrokeModel.pressed_timestamp >= min_time
        )).order_by(KeyStrokeModel.pressed_timestamp).all()

    pressed_keys = [keystroke.key for keystroke in keystrokes]

    print('pressed keys:')
    print(pressed_keys)
    pressed_keys = [decrypt(x) for x in pressed_keys]
    pressed_timestamps = [keystroke.pressed_timestamp for keystroke in keystrokes]
    released_timestamps = [keystroke.released_timestamp for keystroke in keystrokes]

    print('INSIDE VALIDATE USER')
    print(pressed_keys)
    print(pressed_timestamps)
    print(released_timestamps)

    compare_string = "united states"
    index = "".join(pressed_keys).rfind(compare_string)
    print('input:', "".join(pressed_keys))
    print('index:', index)

    if index != -1:
        if not keystroke_model.validate_user(pressed_timestamps[index:index+12], released_timestamps[index:index+12]):
            print('emitting signal...')
            signal.signal_intruder_detected.emit()




def get_typing_speed(user_id):
    keystrokes = db.session.query(KeyStrokeModel).filter(KeyStrokeModel.user_id == user_id).order_by(KeyStrokeModel.pressed_timestamp).all()

    sessions = []
    curr_session = []

    for i in range(len(keystrokes) - 1):
        time_elapsed = keystrokes[i + 1].pressed_timestamp - keystrokes[i].released_timestamp

        if time_elapsed > datetime.timedelta(seconds=2):
            sessions.append(curr_session)
            curr_session = []
        
        curr_session.append(keystrokes[i])

    if len(curr_session):
        sessions.append(curr_session)
    
    word_count_list = []
    time_elapsed_list = []

    for session in sessions:
        session_words_count = 0

        for i in range(len(session)):
            while i < len(session) and (session[i].key != ' '):
                i += 1
            
            if i != 0:
                session_words_count += 1

            while (i < len(session) and session[i].key == ' '):
                i += 1
        
        session_time_elapsed = (session[-1].released_timestamp - session[0].pressed_timestamp) / datetime.timedelta(milliseconds=1)

        if session_time_elapsed <= 0:
            print('ERROR time elapsed less than zero:', session_time_elapsed)
            continue

        time_elapsed_list.append(session_time_elapsed)
        word_count_list.append(session_words_count)

    total_time = sum(word_count_list)
    weighted_word_counts = sum([a*b*1000/a for a, b in zip(time_elapsed_list, word_count_list)])

    if total_time == 0:
        print('total time = 0')
        return 0
    else:
        return weighted_word_counts / total_time

        



def get_flight_time(user_id):
    keystrokes = db.session.query(KeyStrokeModel).filter(KeyStrokeModel.user_id == user_id).order_by(KeyStrokeModel.pressed_timestamp).all()

    time_elapsed_list = []

    for i in range(len(keystrokes) - 1):
        time_elapsed = (keystrokes[i + 1].pressed_timestamp - keystrokes[i].released_timestamp) / datetime.timedelta(seconds=1)

        if time_elapsed > 2:
            continue

        time_elapsed_list.append(time_elapsed)

    total = sum(time_elapsed_list)

    if total == 0:
        return 0
    else:
        return total / len(time_elapsed_list)


def get_duration_keystroke(user_id):
    keystrokes = db.session.query(KeyStrokeModel).filter(KeyStrokeModel.user_id == user_id).order_by(KeyStrokeModel.pressed_timestamp).all()

    time_elapsed_list = []

    for i in range(len(keystrokes)):
        time_elapsed = (keystrokes[i].released_timestamp - keystrokes[i].pressed_timestamp) / datetime.timedelta(milliseconds=1)
        time_elapsed_list.append(time_elapsed)

    print('get duration')
    print(time_elapsed_list)
    total = sum(time_elapsed_list)

    if total == 0:
        return 0
    else:
        return total / len(time_elapsed_list) / 1000


def get_pressure(user_id):
    return None

def get_seek_time(user_id):
    return get_duration_keystroke(user_id) + get_flight_time(user_id)


def start_tracking(user_id, signal):
    print('starting tracking...')
    logger.info('Starting tracking...')

    validate_user(user_id, signal)

    with keyboard.Listener(on_press=lambda x: on_press(x, user_id), on_release=lambda x: on_release(x, user_id, signal)) as listener:
        listener.join()


    