import logging
from sqlalchemy.exc import SQLAlchemyError

import email
from unicodedata import name
from dtos import UserLoginDto, UserDto
from database.models import User as UserModel
from database import db
from security import encrypt, decrypt
import otp

logger = logging.getLogger(__name__)


def login(user: UserLoginDto):
    db_user = db.session.query(UserModel).filter_by(email=user.email).first()

    if db_user is not None: # todo: check
        # check otp code
        if db_user.enable_2fa:
            print('valid otp: ', otp.generate_otp(db_user.otp_secret))
            print('entered otp: ', user.two_fa_code)
            if user.two_fa_code != otp.generate_otp(db_user.otp_secret):
                print('Invalid OTP code')
                return None

        # check password
        if decrypt(db_user.password) == user.password:
            user_dto = UserDto(name=db_user.name, email=db_user.email, phone=db_user.phonenumber, password=db_user.password,\
                                    gender=db_user.gender, country=db_user.country, city=db_user.city, id=db_user.id, enable_2fa=db_user.enable_2fa, otp_secret=db_user.otp_secret)

            return user_dto

    return None


def register(user: UserDto):
    try:
        #exists = db.session.query(UserModel.id).filter_by(name='davidism').first() is not None

        otp_secret = otp.get_random_secret()
        db_user = UserModel(name=user.name, email=user.email, phonenumber=user.phone, \
                            gender=user.gender, country=user.country, city=user.city, password=encrypt(user.password), enable_2fa=user.enable_2fa, otp_secret=otp_secret)

        db.session.add(db_user)
        db.session.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        logger.info(error)

        db.session.rollback()

        return None

    user_dto = UserDto(name=db_user.name, email=db_user.email, phone=db_user.phonenumber, password=db_user.password,\
                            gender=db_user.gender, country=db_user.country, city=db_user.city, enable_2fa=db_user.enable_2fa, otp_secret=otp_secret)
    return user_dto


def get_stats():
    pass

