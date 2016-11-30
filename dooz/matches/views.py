from django.shortcuts import render
from django.shortcuts import render
from matches.forms import MatchForm
from matches.models import Match
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, request
from django.contrib.auth.models import User

# Create your views here.


def create_match(request):
    if request.method == 'POST':
        match_form = MatchForm(data=request.POST)
        match = match_form.save()
        redplr = User()
        blackplr = User()
        for usr in User.objects.all() :
            if  usr.username == match_form.redPlayerName:
                redplr = usr

            if usr.username == match_form.blackPlayerName:
                blackplr = usr

        match.setBlackPlayer(blackplr)
        match.setRedPlayer(redplr)
        match.save()




        match.save()

    else:
        match_form = MatchForm()


    return render(request, 'create_match.html',{'match_form': match_form} )

def get_match(request , match_id):
    for _match in Match.objects.all():
        if _match.id == match_id:
            return HttpResponse()


