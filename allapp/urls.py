from django.conf.urls import url, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from .views import *
app_name = 'allapp'
handler404 = '.views.error_view'


urlpatterns=[
    url(r'^$', index, name="index"),
    url(r'^vacancies/$',job_list, name="job_list"),
    url(r'^job-detail/$',job_detail, name="job_detail"),
    url(r'^aboutus/$',about_us, name="aboutus"),
    url(r'^contact/$',contact_us, name="contact"),

]