# -*- coding: utf-8 -*-
from app import db


class Customer(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    open_id = db.Column('open_id', db.String)

    def __init__(self, open_id):
        self.open_id = open_id

    def __repr__(self):
        return '<Customer %r>' % self.open_id


class MessageReply(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    receive_content = db.Column('req_content', db.String)
    reply_content = db.Column('rep_content', db.String)
    # MsgType

    def __init__(self, receive_content, reply_content):
        self.receive_content = receive_content
        self.reply_content = reply_content
