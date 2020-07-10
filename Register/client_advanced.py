import time
import ast
import mqbeebotte
from . import process_data as pd
from . import config
from .models.models import Envsensor
from .database import init_db,db
import os
from linebot import LineBotApi
from linebot.models import TextSendMessage

data_env=[]
data_co2=[]
data_door=[]
line_bot_api = LineBotApi(config.YOUR_CHANNEL_ACCESS_TOKEN)
user_id = config.YOUR_ID



def on_connect(client, userdata, flags, respons_code):
    print('Connected to Beebotte')
    messages = TextSendMessage(text="接続したよ(heroku)")
    line_bot_api.push_message(user_id, messages=messages)
    return

def on_message(client, userdata, msg):
    #byte型のメッセージを辞書型に変換
    payload_dic = ast.literal_eval(msg.payload.decode('utf-8'))

    #それそれのデータリストに追加していく。
    if 'envsensor' in msg.topic:
        get_data = pd.process_env(payload_dic)
        data_env.append(get_data)

        #herokuのDBにセンサーデータを代入
        envsensor = Envsensor(
            data_id = get_data['data_id'],
            sensor_id = get_data['sensor_id'],
            temperature = get_data['temperature'],
            humidity = get_data['humidity'],
            light = get_data['light'],
            heat = get_data['heat'],
            di = get_data['di'],
            noise = get_data['noise']
        )
        db.session.add(envsensor)
        db.session.commit()


    elif 'co2mini' in msg.topic:
        data_co2.append(pd.process_co2(payload_dic))

    else:
        data_door.append(pd.process_door(payload_dic))

    print(data_env)
    print(data_co2)
    print(data_door) 

    return



client = mqbeebotte.client()

client.connect(config.CHANNEL_TOKEN, on_connect=on_connect, on_message=on_message)