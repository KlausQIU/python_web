# !/usr/bin/env python
# -*- coding:utf-8 -*-

from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.shortcuts import render,render_to_response,get_object_or_404  
from django.template import RequestContext
from models import User,Experience,skill,introduction,Education
from .form import LoginPage
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout


from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.contrib.auth.decorators import login_required
import re

class LoginBackend(object):
    def authenticate(self, username=None, password=None):
        if username:
            #email
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", username) != None:
                try:
                    user = User.objects.get(username=username)
                    if user.check_password(password):
                        return user
                except User.DoesNotExist:
                    return None
            #mobile
            elif len(username)==11 and re.match("^(1[3458]\d{9})$", username) != None:
                try:
                    user = User.objects.get(mobile=username)
                    if user.check_password(password):
                        return user
                except User.DoesNotExist:
                    return None  
            #nick
            else:
                try:
                    user = User.objects.get(username=username)
                    if user.check_password(password):
                        return user
                except User.DoesNotExist:
                    return None                
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

def login_test_username(username,password):
	try:
		user = User.objects.get(name = username)
		if user.password == password:
			return True
	except User.DoesNotExist:
		return False


def login_validate(request,username,password):
  rtvalue = False
  #user = authenticate(username=username,password=password)
  if user is not None:
    if user.is_active:
      user = User.objects.get(name=username)
      return True
  return rtvalue

#login	
def index(request):
	return render(request,'index.html')

def login(request):
	error = []
	'''
	if request.method == 'POST':
		username = request.POST.get('username')
		user = User.objects.filter(username__exact = username,password__exact = password)
		if user:
				response = HttpResponseRedirect('/index/')
				response.set_cookie('username',username,3600)
				return response
			else:
				return HttpResponseRedirect('/login/')
		else:
			uf = UserForm()
		return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(request))
	return render(request, 'login.html')
	'''
	if request.method == 'POST':
		form = LoginPage(request.POST)
		if form.is_valid():
			data = form.cleaned_data
      		username = data['username']
      		password = data['password']
        	return render_to_response('index.html')
    	else:
      		error.append('Please input both username and password')
  	return render_to_response('login.html',{'error':error,'form':form})

def register(request):
	return render(request,'register.html')

def base(request):
	return render_to_response('base.html',RequestContext(request))


def login_test(request):
	form = LoginPage()
	error = []
	if request.method == 'POST':
		form = LoginPage(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			username = data['username']
			password = data['password']
			if login_test_username(username,password):
				user = User.objects.get(name=username)
				company1 = Experience.objects.get(company=user.user_experience.all()[0])
				company2 = Experience.objects.get(company=user.user_experience.all()[1])
				return render_to_response('index.html',{
					'username':username,
					'phonenumber':user.phonenumber,
					'email':user.email,
					'address':user.address,
					'company1':user.user_experience.all()[0],
					'starttime1':company1.starttime,
					'position1':company1.position,
					'company2':user.user_experience.all()[1],
					})
			else:
				error.append('Please input the correct password')
		else:
			error.append('Please input both username and password')
	else:
		form = LoginPage()
	return render_to_response('login_test.html',{'error':error,'form':LoginPage})






