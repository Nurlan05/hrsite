from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from allapp.models import AboutUs,ContactUs,CvSend,Job,Location,Sector,JobType,ExperienceLevel,ContractType,Hours
from allapp.form import CvSendForm
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from .filters import JobFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	context={}
	context['contactus']=ContactUs.objects.all()
	context['last_job']=Job.objects.filter(draft=True)[:12]
	return render(request,'home/home.html',context)


def job_list(request):
	context={}
	context['contactus']=ContactUs.objects.all()
	job_list=Job.objects.filter(draft=True)
	context['location_list']=Location.objects.all()
	context['sector_list']=Sector.objects.all()
	context['job_type_list']=JobType.objects.all()
	context['experience_level_list']=ExperienceLevel.objects.all()
	context['hours_list']=Hours.objects.all()
	context['contract_type_list']=ContractType.objects.all()
	filter=JobFilter(request.GET,queryset=job_list)
	context['filter']=filter
	job_list=Job.objects.filter(draft=True)
	query=request.GET.get('q')
	if query:

		sel_location=request.GET.get('location',None)
		if sel_location:
			location=get_object_or_404(Location,pk=sel_location)
			if location:
				context['jobs']=job_list.filter(job_location__city_name__icontains=query).distinct()
			job_list=job_list.filter(
				Q(title__icontains=query)
				).distinct()
	paginator = Paginator(job_list, 10000)
	page = request.GET.get('page')
	try:
		context['jobs'] = paginator.page(page)
	except PageNotAnInteger:
		context['jobs'] = paginator.page(1)
	except EmptyPage:
		context['jobs'] = paginator.page(paginator.num_pages)
	return render(request,'job/job-list.html',context)



def location_view(request,slug):
	loc=get_object_or_404(Location,slug=slug)
	context={}
	context['contactus']=ContactUs.objects.all()
	context['topic_name']=loc.city_name
	context['alljobs']=loc.location.all()
	context['job_count']=loc.location.all().count()
	context['location_list']=Location.objects.all()
	context['sector_list']=Sector.objects.all()
	context['job_type_list']=JobType.objects.all()
	context['experience_level_list']=ExperienceLevel.objects.all()
	context['hours_list']=Hours.objects.all()
	context['contract_type_list']=ContractType.objects.all()
	return render(request,'job/location-list.html',context)


def jobtype_view(request,slug):
	loc=get_object_or_404(JobType,slug=slug)
	context={}
	context['contactus']=ContactUs.objects.all()
	context['topic_name']=loc.job_name
	context['alljobs']=loc.jobtype.all()
	context['job_count']=loc.jobtype.all().count()
	context['location_list']=Location.objects.all()
	context['sector_list']=Sector.objects.all()
	context['job_type_list']=JobType.objects.all()
	context['experience_level_list']=ExperienceLevel.objects.all()
	context['hours_list']=Hours.objects.all()
	context['contract_type_list']=ContractType.objects.all()
	return render(request,'job/jobtype-list.html',context)


def sector_view(request,slug):
	loc=get_object_or_404(Sector,slug=slug)
	context={}
	context['contactus']=ContactUs.objects.all()
	context['topic_name']=loc.sector_name
	context['alljobs']=loc.sector.filter(draft=True)
	context['job_count']=loc.sector.filter(draft=True).count()
	context['location_list']=Location.objects.all()
	context['sector_list']=Sector.objects.all()
	context['job_type_list']=JobType.objects.all()
	context['experience_level_list']=ExperienceLevel.objects.all()
	context['hours_list']=Hours.objects.all()
	context['contract_type_list']=ContractType.objects.all()
	return render(request,'job/sector-list.html',context)


def contract_view(request,slug):
	loc=get_object_or_404(ContractType,slug=slug)
	context={}
	context['contactus']=ContactUs.objects.all()
	context['topic_name']=loc.contract_name
	context['alljobs']=loc.contracttype.filter(draft=True)
	context['job_count']=loc.contracttype.filter(draft=True).count()
	context['location_list']=Location.objects.all()
	context['sector_list']=Sector.objects.all()
	context['job_type_list']=JobType.objects.all()
	context['experience_level_list']=ExperienceLevel.objects.all()
	context['hours_list']=Hours.objects.all()
	context['contract_type_list']=ContractType.objects.all()
	return render(request,'job/contract-list.html',context)


def hours_view(request,slug):
	loc=get_object_or_404(Hours,slug=slug)
	context={}
	context['contactus']=ContactUs.objects.all()
	context['topic_name']=loc.hours_name
	context['alljobs']=loc.hours.filter(draft=True)
	context['job_count']=loc.hours.filter(draft=True).count()
	context['location_list']=Location.objects.all()
	context['sector_list']=Sector.objects.all()
	context['job_type_list']=JobType.objects.all()
	context['experience_level_list']=ExperienceLevel.objects.all()
	context['hours_list']=Hours.objects.all()
	context['contract_type_list']=ContractType.objects.all()
	return render(request,'job/hours-list.html',context)


def experience_view(request,slug):
	loc=get_object_or_404(ExperienceLevel,slug=slug)
	context={}
	context['contactus']=ContactUs.objects.all()
	context['topic_name']=loc.experience_name
	context['alljobs']=loc.experiencelevel.filter(draft=True)
	context['job_count']=loc.experiencelevel.filter(draft=True).count()
	context['location_list']=Location.objects.all()
	context['sector_list']=Sector.objects.all()
	context['job_type_list']=JobType.objects.all()
	context['experience_level_list']=ExperienceLevel.objects.all()
	context['hours_list']=Hours.objects.all()
	context['contract_type_list']=ContractType.objects.all()
	return render(request,'job/experience-list.html',context)

def job_detail(request,slug):
	job=get_object_or_404(Job,slug=slug)
	context={}
	context['contactus']=ContactUs.objects.all()
	context['job_list']=Job.objects.filter(draft=True).exclude(pk=job.id)[:3]
	context['obj']=job
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
	return render(request,'job/job-detal.html',context)

def job_cv_detail(request,slug):
	job=get_object_or_404(Job,slug=slug)
	context={}
	context['contactus']=ContactUs.objects.all()
	context['job_list']=Job.objects.filter(draft=True).exclude(pk=job.id)[:3]
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
	context['aboutus']=AboutUs.objects.all()
	context['contactus']=ContactUs.objects.all()
	return render(request,'aboutus/aboutus.html',context)
def contact_us(request):
	context={}
	context['contactus']=ContactUs.objects.all()
	return render(request,'contact/contact.html',context)
def cv_list_view(request):
	context={}
	context['cv_list']=CvSend.objects.all()
	return render(request,'job/cv-list.html',context)
	context['contactus']=ContactUs.objects.all()
