from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    redPlayer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='red_match')
    blackPlayer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='black_match')

    matchTime = models.DateTimeField(blank=False)

    has_ended = models.BooleanField(blank=True, default=False)
    history = models.CommaSeparatedIntegerField(max_length=16, blank=True, default=[])

    def setRedPlayer(self , user):
        self.redPlayer = user


    def setBlackPlayer(self , user):
        self.blackPlayer = user

    def __str__(self):
        return redPlayer + ' ' + blackPlayer

    def save(self , *args , **kwargs):
        super(Match , self).save(*args , **kwargs)

