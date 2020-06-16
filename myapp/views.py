# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from myapp.models import *
from django.shortcuts import render


# Create your views here.


def registration(request):
    return render(request, 'registration.html')


def setpassword(request):
    return render(request, 'setpassword.html')


def setpassworddone(request):
    if request.method == 'POST':
        try:
            mobile = request.POST.get('your_mobile')
            newpass = request.POST.get('your_npassword')
            confpass = request.POST.get('your_cpassword')
        except:
            data = {'success': 'setpasswordfield', 'message': 'All fields are compulsory'}
            return HttpResponse(json.dumps(data), content_type='application/json')
        if mobile == "" or newpass == "" or confpass == "":
            data = {'success': 'setpasswordfield', 'message': 'All fields are compulsory'}
            return HttpResponse(json.dumps(data), content_type='application/json')
        if not mobile.isdigit():
            data = {'success': 'digitrequire', 'message': 'Mobile No. Must Be In Digits'}
            return HttpResponse(json.dumps(data), content_type='application/json')
        if len(mobile) != 10:
            data = {'success': 'digitlimit', 'message': 'Mobile No. Must Have 10 Digits'}
            return HttpResponse(json.dumps(data), content_type='application/json')

        try:
            user = User.objects.get(username=mobile)
        except:
            data = {'success': 'invalidmob', 'message': 'Invalid Mobile No.'}
            return HttpResponse(json.dumps(data), content_type='application/json')
        if newpass != confpass:
            data = {'success': 'passnotmatch', 'message': 'Password Not Matches'}
            return HttpResponse(json.dumps(data), content_type='application/json')
        user.set_password(confpass)
        user.save()
        data = {'success': 'true', 'message': 'Password set Successfully!!'}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        data = {'success': 'noPost', 'message': 'Not a Post method'}
        return HttpResponse(json.dumps(data), content_type='application/json')


def login1(request):
    return render(request, 'login.html')


def mainpage(request):
    data = request.GET.get('name')
    name = {"members": data}
    return render(request, 'index.html', name)

def home(request):
    if request.method == 'POST':

        try:
            username = request.POST.get('your_username')
            password = request.POST.get('your_password')
        except:
            data = {'success': 'loginfield', 'message': 'Please enter your username and password'}
            return HttpResponse(json.dumps(data), content_type='application/json')
        if username == "" and password == "":
            data = {'success': 'loginfield', 'message': 'Please enter your username and password'}
            return HttpResponse(json.dumps(data), content_type='application/json')

        user = User.objects.filter(username=username)
        if not user.exists():
            data = {'success': 'invalidusername', 'message': 'Invalid Username or Password'}
            return HttpResponse(json.dumps(data), content_type='application/json')
        if not user[0].is_active:
            data = {'success': 'userinactive', 'message': 'User Not Active'}
            return HttpResponse(json.dumps(data), content_type='application/json')
        user1 = auth.authenticate(username=username, password=password)
        if not user1:
            data = {'success': 'wrongpass', 'message': 'Wrong Password'}
            return HttpResponse(json.dumps(data), content_type='application/json')
        data = {'success': 'true', 'members': user[0].employee.name}
        return HttpResponse(json.dumps(data), content_type='application/json')

    else:
        data = {'success': 'noPost', 'message': 'Not a Post method'}
        return HttpResponse(json.dumps(data), content_type='application/json')


def registersuccess(request):
    if request.method == 'POST':
        try:
            mobile = request.POST.get('your_mobile')
            name = request.POST.get('your_name')
            email = request.POST.get('your_email')
            gender = request.POST.get('your_gender')
            address = request.POST.get('your_address')
            designation = request.POST.get('your_des')
        except:
            data = {'success': 'registerfield', 'message': 'All fields are compulsory'}
            return HttpResponse(json.dumps(data), content_type='application/json')
        if mobile == "" or name == "" or email == "" or address == "" or designation == "":
            data = {'success': 'registerfield', 'message': 'All fields are compulsory'}
            return HttpResponse(json.dumps(data), content_type='application/json')
        if not mobile.isdigit():
            data = {'success': 'digitrequire', 'message': 'Mobile No. Must Be In Digits'}
            return HttpResponse(json.dumps(data), content_type='application/json')
        if len(mobile) != 10:
            data = {'success': 'digitlimit', 'message': 'Mobile No. Must Have 10 Digits'}
            return HttpResponse(json.dumps(data), content_type='application/json')

        user, create = User.objects.get_or_create(username=mobile)
        user.save()

        user.email = email
        user.save()
        try:
            userprofile, create = Employee.objects.update_or_create(user_id_id=user.id,
                                                                    defaults={"name": name,
                                                                              "gender": gender, "address": address,
                                                                              "designation": designation,
                                                                              })
        except Exception as e:
            print(e)
            data = {'success': 'false', 'message': 'Something went wrong'}
            return HttpResponse(json.dumps(data), content_type='application/json')
        data = {'success': 'true', 'message': 'User is added successfully'}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        data = {'success': 'noPost', 'message': 'Not a Post method'}
        return HttpResponse(json.dumps(data), content_type='application/json')
