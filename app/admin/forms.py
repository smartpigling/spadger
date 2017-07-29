# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, \
    TextAreaField, RadioField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo, Email
from app.admin.models.users import User


class UserForm(FlaskForm):
    email = StringField('账号', validators=[Length(min=5, max=50)])
    password = PasswordField('密码', validators=[DataRequired('密码不能为空'),
            Length(min=8, max=20), EqualTo('confirm_password', message='密码必须匹配')])
    confirm_password = PasswordField('重复密码')
    # email = StringField('邮件地址', validators=[Email(
    #     message='请输入有效的邮箱地址，如：username@domain.com')])
    submit = SubmitField('确认')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已被注册')

    # def validate_email(self, field):
    #     if User.query.filter_by(email=field.data).first():
    #         raise ValidationError('邮箱已被注册')


