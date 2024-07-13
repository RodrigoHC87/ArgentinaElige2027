import os


class Config:
    SECRET_KEY = 'my_secret_key'
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username="root",
        password="",
        hostname="localhost",
        databasename="argentina_elige_local",
    )

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 299
