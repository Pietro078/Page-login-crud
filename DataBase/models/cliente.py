from peewee import CharField, Model, DateField
from DataBase.database import db

class Cliente(Model):
    email = CharField(unique=True)
    senha = CharField()

    class Meta:
        database = db 