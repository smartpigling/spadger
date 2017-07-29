# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, EqualTo


class MessageReplyForm(FlaskForm):
    receive_content = StringField('接收', validators=[DataRequired('必须填写')])
    reply_content = StringField('答复', validators=[DataRequired('必须填写')])