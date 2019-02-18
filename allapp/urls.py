from django.conf.urls import url, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from .views import *
app_name = 'allapp'
handler404 = '.views.error_view'


urlpatterns=[
    url(r'^$', index, name="index"),
    url(r'^vakansiyalar/$',job_list, name="job_list"),
    url(r'^detal/(?P<slug>.*)/$',  job_detail, name="job_detail"),
    url(r'^haqqimizda/$',about_us, name="aboutus"),
    url(r'^elaqe/$',contact_us, name="contact"),
    url(r'^cv-list/$',cv_list_view, name="cv-list")

]