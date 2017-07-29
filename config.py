import os

class BaseConfig(object):
    # Flask Config
    SECRET_KEY = b'D\xfc2\xdf\x18\xb2\xd2d\xf9\xae\xeb\xa7\xc4\xba\xd5\xec9\x89\xae\xf9\xcf\x18M'
    SECURITY_PASSWORD_SALT = 'SALT'
    SECURITY_POST_LOGIN_VIEW = '/admin/'
    SECURITY_POST_LOGOUT_VIEW = '/login'
    # Pagination
    PER_PAGE = 20
    CSS_FRAMEWORK = 'bootstrap3'
    LINK_SIZE = 'sm'
    SHOW_SINGLE_PAGE = False

    # WeiXin
    HOST = '0.0.0.0'
    PORT = 80
    TOKEN = 'WEIXINTEST'
    APP_ID = 'wx695ca7a97b522c80'
    APP_SECRET = '1abbac18ac29e4668e901cd66715cbd8'
    ENCODING_AES_KEY = ''

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # DB Config
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/dev.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(BaseConfig):
    @classmethod
    def init_app(cls, app):
        BaseConfig.init_app(app)

        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)

config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig,
    'default': DevelopmentConfig
}