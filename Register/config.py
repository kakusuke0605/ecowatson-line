# -*- coding: utf-8 -*-
import os


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


#LINEチャンネル設定
Channel_access_token = 'EhgLPLw7EebpxdbqX0SjpSScFqRdfq0eco2R7f/PW5FBu+CgFpdssSqjwrOMmpaqkzH1gIRHsbugdmlgrmK8sTgJzeb9bb+6bzmqkft1qnPsC4Fjkw37PyJW7HergBgt0pTz0tqiMzpeVnWeFrCxXQdB04t89/1O/w1cDnyilFU='

Channel_secret = '215ea75cc2e6fb65e3ff26f602a45de0'
