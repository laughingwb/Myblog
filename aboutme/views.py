from django.shortcuts import render,render_to_response
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import Myself,Technical,UseTechnial
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from rest_framework.authtoken import views
from django.contrib.auth import logout,login
from mylife.models import Aricletype

# Create your views here.
def myselfinfo(request):
    myself = Myself.objects.all();
    useTechniallist = UseTechnial.objects.filter(myself=myself)
    return render(request, 'myself.html',{'myselfInfo':myself[0],'useTechniallist':useTechniallist})

def login_man(request):
    return render(request, 'login.html')

def man_home(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print('username====' + username)
    print('password====' + password)
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            print("User is valid, active and authenticated")
            login(request, user)
            typeAll = Aricletype.objects.all();
            return render(request, 'man/lifemanage.html',{'typeList': typeAll})
        else:
            return render(request,"login.html", {'code':'login failed'})
    else:
        # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")
        return render(request,"login.html", {'code': 'The username and password were incorrect.'})

def loginout(request):
    logout(request)
    return render(request, 'login.html')

@login_required()
def messagemanage(request):
    return render(request, 'man/messagemanage.html')

@login_required()
def techmanage(request):
    return render(request, 'man/techmanage.html')

@login_required()
def myinfomanage(request):
    return render(request, 'man/myinfomanage.html')

