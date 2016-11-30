from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    code = models.TextField(max_length=None, blank=True)
    language = models.CharField(max_length=10, blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username

class Match(models.Model):
    redPlayer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='red_match')
    blackPlayer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='black_match')

    matchTime = models.DateTimeField(blank=False)

    has_ended = models.BooleanField(blank=True, default=False)
    history = models.CommaSeparatedIntegerField(max_length=16, blank=True, default=[])

    def __str__(self):
        return redPlayer + ' ' + blackPlayer
