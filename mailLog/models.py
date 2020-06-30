from django.db import models
from mongoengine import *
from datetime import datetime
# Create your models here.
class maillog(EmbeddedDocument):
    local = StringField(required=True)
    date = DateTimeField(required=True)
    service = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    