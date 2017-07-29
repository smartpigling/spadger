# -*- coding:utf-8 -*-
import os
from app import create_app, db
from flask import url_for
from flask_script import Manager, Server
from flask_script.commands import ShowUrls, Clean
from flask_migrate import Migrate, MigrateCommand
from flask_security.utils import hash_password
from uuid import uuid4 as uuid
from app.admin.models import users
from app.weixin.models import general

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


# manager.add_option('-c', '--config', dest='config_name', default='default')
manager.add_command('db', MigrateCommand)
manager.add_command('urls', ShowUrls())
manager.add_command('clean', Clean())
manager.add_command('runserver', Server(host='0.0.0.0', port=80))


@manager.command
def init():
    """Project init"""
    # init User Role
    user = users.User(
        id=str(uuid()),
        email='admin',
        password=hash_password('admin'),
        active=True
    )
    role = users.Role(
        id=str(uuid()),
        name='superuser'
    )
    auth1 = users.Authority(
        id=str(uuid()),
        name='首页',
        type='M',
        active=True,
        path=url_for('admin.home')
    )
    auth2 = users.Authority(
        id=str(uuid()),
        name='测试',
        type='M',
        active=True,
        path=url_for('admin.test')
    )
    auth3 = users.Authority(
        id=str(uuid()),
        name='test',
        type='M',
        active=True,
        path=url_for('admin.test')
    )
    auth3.authority_id=auth1.id
    role.authorities.append(auth1)
    role.authorities.append(auth2)
    role.authorities.append(auth3)
    user.roles.append(role)
    db.session.add(user)
    db.session.commit()


@manager.command
def deploy():
    """Run deployment tasks."""
    from flask_migrate import init, migrate, upgrade
    try:
        init()
    except:
        pass
    migrate()
    upgrade()


@manager.command
def drop():
    db.drop_all()


@manager.shell
def make_shell_context():
    """
    Create a python CLI.
    return: Default import object
    type: `Dict`
    """
    from app.admin.models import users
    return dict(app=manager.app,
                db=db,
                User=users.User,
                Group=users.Group,
                Role=users.Role,
                Authority=users.Authority)


if __name__ == '__main__':
    manager.run()
