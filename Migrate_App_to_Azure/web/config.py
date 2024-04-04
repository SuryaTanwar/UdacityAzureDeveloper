import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = True
    # TODO: Update value
    POSTGRES_URL = "techconf-postgres-db-server.postgres.database.azure.com"
    POSTGRES_USER = "postgresAdmin@techconf-postgres-db-server"  # TODO: Update value
    POSTGRES_PW = "single123@"  # TODO: Update value
    POSTGRES_DB = "techconfdb"  # TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING = 'Endpoint=sb://techconfsb.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=deWoB2kIDZyVHuMIDXj5tV6ErqAA1goq5DSCyQUwads='  # TODO: Update value
    SERVICE_BUS_QUEUE_NAME = 'notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    SENDGRID_API_KEY = ''  # Configuration not required, required SendGrid Account


class DevelopmentConfig(BaseConfig):
    DEBUG = False


class ProductionConfig(BaseConfig):
    DEBUG = True
