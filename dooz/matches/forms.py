from matches.models import Match
from django.contrib.auth.models import User
from django import forms

class MatchForm(forms.ModelForm):
    redPlayerName = forms.CharField(max_length=100)
    blackPlayerName = forms.CharField(max_length=100)
    class Meta:
        model = Match
        fields = ('id', 'redPlayer', 'blackPlayer')






