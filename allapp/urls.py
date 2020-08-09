from django.conf.urls import url, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from .views import *
app_name = 'allapp'
handler404 = '.views.error_view'


urlpatterns=[
    url(r'^$', index, name="index"),
    url(r'^detal/(?P<slug>.*)/apply/$',  job_cv_detail, name="job_cv_detail"),

    url(r'^vakansiyalar/$',job_list, name="job_list"),
    url(r'^detal/(?P<slug>.*)/$',  job_detail, name="job_detail"),

    url(r'^yer/(?P<slug>.*)/$',  location_view, name="location_view"),
    url(r'^kontrakt/(?P<slug>.*)/$',  contract_view, name="contract_view"),
    url(r'^is-novu/(?P<slug>.*)/$',  jobtype_view, name="jobtype_view"),
    url(r'^novbe/(?P<slug>.*)/$', hours_view, name="hours_view"),
    url(r'^tecrube/(?P<slug>.*)/$',  experience_view, name="experience_view"),
    url(r'^sektor/(?P<slug>.*)/$',  sector_view, name="sector_view"),

    url(r'^haqqimizda/$',about_us, name="aboutus"),
    url(r'^elaqe/$',contact_us, name="contact"),
    url(r'^cv-list/$',cv_list_view, name="cv-list"),

    url(r'^resetFilters/$',reset_filters,name='reset-filters'),

]