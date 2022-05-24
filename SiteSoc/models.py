from django.db import models


class ChatHistory(models.Model):
    message = models.TextField()
    username = models.TextField()
    date = models.DateTimeField()
