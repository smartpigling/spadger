# -*- coding: utf-8 -*-
from app import db
from flask_security import UserMixin, RoleMixin

users_roles = db.Table('users_roles',
                       db.Column('user_id', db.String(45), db.ForeignKey('users.id')),
                       db.Column('role_id', db.String(45), db.ForeignKey('roles.id')))

groups_users = db.Table('groups_users',
                        db.Column('user_id', db.String(45), db.ForeignKey('users.id')),
                        db.Column('group_id', db.String(45), db.ForeignKey('groups.id')))

roles_authorities = db.Table('roles_authorities',
                             db.Column('role_id', db.String(45), db.ForeignKey('roles.id')),
                             db.Column('authority_id', db.String(45), db.ForeignKey('authorities.id')))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    email = db.Column(db.String(100), unique=True)
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(63))
    current_login_ip = db.Column(db.String(63))
    login_count = db.Column(db.Integer)

    roles = db.relationship('Role',
                            secondary=users_roles,
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<Model User {}>'.format(self.username)


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'

    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))

    authorities = db.relationship('Authority',
                                  secondary=roles_authorities,
                                  backref=db.backref('roles', lazy='dynamic'))

    def __repr__(self):
        return '<Model Role {}>'.format(self.name)


class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(100))
    users = db.relationship('User',
                            secondary=groups_users,
                            backref=db.backref('groups', lazy='dynamic'))

    def __repr__(self):
        return '<Model Group {}>'.format(self.name)


class Authority(db.Model):
    __tablename__ = 'authorities'

    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(100))
    path = db.Column(db.String(255))
    type = db.Column(db.String(1)) #M:Menu, B:Button
    active = db.Column(db.Boolean())
    authority_id = db.Column(db.String(45), db.ForeignKey('authorities.id'))

    def __repr__(self):
        return '<Model Authority {}>'.format(self.name)
