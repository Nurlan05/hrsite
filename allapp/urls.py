from django.conf.urls import url, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from .views import *
app_name = 'allapp'
handler404 = '.views.error_view'


urlpatterns=[
    url(r'^$', index, name="index"),

]