# -*- coding:utf-8 -*-
import werobot
from flask import Flask, request, url_for
from config import config, BaseConfig
from flask_sqlalchemy import SQLAlchemy
from werobot.contrib.flask import make_view
from flask_security import Security, SQLAlchemyUserDatastore
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_security import current_user
from flask_principal import Principal, identity_loaded, Permission, UserNeed, RoleNeed, ActionNeed
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from flask_menu import Menu, MenuEntryMixin, register_menu ,current_menu


db = SQLAlchemy()
nav = Nav()
robot = werobot.WeRoBot(token=BaseConfig.TOKEN,
                        app_id=BaseConfig.APP_ID,
                        app_secret=BaseConfig.APP_SECRET)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # SQLAlchemy
    db.init_app(app)
    # Bootstrap
    Bootstrap(app)
    # Nav
    nav.init_app(app)
    # Flask Security
    from app.admin.models.users import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        identity.user = current_user

        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                for authority in role.authorities:
                    identity.provides.add(ActionNeed(authority.name))

    # Blueprint Admin
    from app.admin.views.admin import admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from app.weixin.views.main import weixin_blueprint
    app.register_blueprint(weixin_blueprint, url_prefix='/weixin')
    # WeiXin
    app.add_url_rule(rule='/robot/', endpoint='werobot',
                     view_func=make_view(robot), methods=['GET', 'POST'])

    return app


@nav.navigation()
def top_nav():
    items = [View('Home', 'admin.home'), View('test', 'admin.test')]

    return Navbar('navbar', *items)




