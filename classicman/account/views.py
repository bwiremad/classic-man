# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import auth
from account.forms import RegistrationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'account/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'account/registrationform.html', args)

def registered(request):
    return render(request, 'account/registered.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")

@login_required
def logout(request):
    return HttpResponseRedirect('/account/')













































