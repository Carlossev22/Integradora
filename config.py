from decouple import config

class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST='coveldb.crpztcwucjwd.us-east-1.rds.amazonaws.com'
    MYSQL_USER='Sevilla'
    MYSQL_PASSWORD='Carlos2510'
    MYSQL_DB='tienda'
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME='20213tn043@utez.edu.mx'
    MAIL_PASSWORD=config('MAIL_PASSWORD')


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
