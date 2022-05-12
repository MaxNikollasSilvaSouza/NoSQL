from typing_extensions import Required
from mongoengine import *
from mongoengine.document import Document
from mongoengine.fields import IntField, StringField

#Cria uma collection no banco de dados
class Repository(Document):

    usuario = StringField(Required = True)
    repositorio = StringField(Required= True)
  

