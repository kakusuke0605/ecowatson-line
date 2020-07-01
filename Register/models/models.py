# -*- coding: utf-8 -*-
from datetime import datetime
from Register.database import db


class Message(db.Model):

    __tablename__ = 'message'

    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    line_user_id=db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<message_id = {message_id}, line_user_id = {line_user_id}, message = {message}>'.format(
            message_id=self.message_id,
            line_user_id=self.line_user_id,
            message=self.message
        )


class Envsensor(db.Model):

    __tablename__ = 'envsensor'

    data_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sensor_id=db.Column(db.Float(255), nullable=False)
    temperature = db.Column(db.Float(255), nullable=False)
    humidity = db.Column(db.Float(255), nullable=False)
    light = db.Column(db.Float(255), nullable=False)
    heat = db.Column(db.Float(255), nullable=False)
    di = db.Column(db.Float(255), nullable=False)
    noise = db.Column(db.Float(255), nullable=False)


    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<data_id = {data_id}, line_user_id = {sensor_id}, temperature = {temperature} , humidity  = {humidity} , light = {light} , heat = {heat} , di = {di} , noise = {noise}>'.format(
            data_id=self.data_id,
            sensor_id=self.sensor_id,
            temperature=self.temperature,
            humidity=self.humidity,
            light=self.light,
            heat=self.heat,
            di=self.di,
            noise=self.noise
        )