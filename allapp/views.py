from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from allapp.models import CvSend,Job,Location,Sector,JobType,ExperienceLevel,ContractType,Hours
from allapp.form import CvSendForm
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _



def index(request):
	context={}
	context['last_job']=Job.objects.all()[:10]
	return render(request,'home/home.html',context)


def job_list(request):
	context={}
	context['job_list']=Job.objects.all()
	return render(request,'job/job-list.html',context)

def job_detail(request,slug):
	job=get_object_or_404(Job,slug=slug)
	context={}
	context['job_list']=Job.objects.all().exclude(pk=job.id)[:3]
	context['job']=job
	if request.method=='POST':
		form=CvSendForm(request.POST,request.FILES or None)

		if form.is_valid():
			cv=form.save()
			cv.apply_for=job.slug
			cv.save()
			messages.success(request,_('Məlumatlarınız uğurla göndərildi!'))
			return redirect(job.get_absolute_url())
	else:
		form=CvSendForm()
		context['form']=form
	return render(request,'job/job-detal.html',context)

def job_cv_detail(request,slug):
	job=get_object_or_404(Job,slug=slug)
	context={}
	context['job_list']=Job.objects.all().exclude(pk=job.id)[:3]
	context['job']=job
	if request.method=='POST':
		form=CvSendForm(request.POST,request.FILES or None)

		if form.is_valid():
			cv=form.save()
			cv.apply_name=job.title
			cv.apply_for=job.slug
			cv.save()
			messages.success(request,_('Məlumatlarınız uğurla göndərildi!'))
			return redirect(job.get_absolute_url())
	else:
		form=CvSendForm()
		context['form']=form
	return render(request,'job/apply-detal.html',context)
def about_us(request):
	context={}
	return render(request,'aboutus/aboutus.html',context)
def contact_us(request):
	context={}
	return render(request,'contact/contact.html',context)
def cv_list_view(request):
	context={}
	context['cv_list']=CvSend.objects.all()
	return render(request,'job/cv-list.html',context)