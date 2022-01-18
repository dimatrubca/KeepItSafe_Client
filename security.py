from cryptography.fernet import Fernet
from dotenv import load_dotenv
from os.path import join, dirname
import os


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
cypher_suite = Fernet(os.environ['key'])

def encrypt(mess):
    encrypted_mess = cypher_suite.encrypt(str(mess).encode('utf-8'))   

    return encrypted_mess

def decrypt(mess):
    return cypher_suite.decrypt(mess).decode('utf-8')