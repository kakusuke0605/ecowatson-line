# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
load_dotenv()

class DevelopmentConfig:
    # Flask
    DEBUG = True

    #MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4'.format(**{
        'user': os.getenv('DB_USER', 'b5ce340141e1f5'),
        'password': os.getenv('DB_PASSWORD', '969a6a56'),
        'host': os.getenv('DB_HOST', 'us-cdbr-east-02.cleardb.com'),
        'database': os.getenv('DB_DATABASE', 'heroku_9de8a2b86d37394')
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig

YOUR_CHANNEL_ACCESS_TOKEN = os.getenv('YOUR_CHANNEL_ACCESS_TOKEN')
YOUR_CHANNEL_SECRET = os.getenv('YOUR_CHANNEL_SECRET')
CHANNEL_TOKEN = os.getenv('CHANNEL_TOKEN')
TOPIC_BASE = os.getenv('TOPIC_BASE')
UNIT = os.getenv('UNIT')