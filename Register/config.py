# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
load_dotenv()

class DevelopmentConfig:
    # Flask
    DEBUG = True

    #MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4'.format(**{
        'user': os.getenv('DB_USERNAME'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOSTNAME'),
        'database': os.getenv('DB_NAME')
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig

YOUR_CHANNEL_ACCESS_TOKEN = os.getenv('YOUR_CHANNEL_ACCESS_TOKEN')
YOUR_CHANNEL_SECRET = os.getenv('YOUR_CHANNEL_SECRET')
CHANNEL_TOKEN = os.getenv('CHANNEL_TOKEN')
TOPIC_BASE = os.getenv('TOPIC_BASE')
UNIT = os.getenv('UNIT')
YOUR_ID = os.getenv('YOUR_ID')