from django.conf.urls import url
from django.contrib import admin
from myapp.views import *
urlpatterns = [
    url(r'^registration/', registration),
    url(r'^registersuccess/', registersuccess),
    url(r'^setpassword/', setpassword),
    url(r'^setpassworddone/', setpassworddone),
    url(r'^login/', login1),
    url(r'^home/', home),
    url(r'^mainpage/', mainpage)

]