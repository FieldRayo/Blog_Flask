class Config:
    DEBUG = True
    TESTING = True

    # Data base config
    SQLACEMY_TRACK_MODIFICATIONS = False
    SQLACHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3306/blog_db"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    SECRET_KEY = 'dev'
    DEBUG = True
    TESTING = True

