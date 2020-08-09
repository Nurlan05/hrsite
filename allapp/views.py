from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from allapp.models import AboutUs,ContactUs,CvSend,Job,Location,Sector,JobType,ExperienceLevel,ContractType,Hours,Industry
from allapp.form import CvSendForm
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from .filters import JobFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.template.loader import render_to_string


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
	context['industry_list']=Industry.objects.all()
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


def reset_filters(request):
	data={}
	jtls = JobType.objects.all()
	ells = ExperienceLevel.objects.all()
	ils = Industry.objects.all()
	jtls_list = []
	ells_list = []
	ils_list = []
	for jtl in jtls:
		id_ = str(jtl.id)
		try:
			jtls_list.append(request.POST['jtl-'+id_])
		except:
			pass
	for ell in ells:
		id_ = str(ell.id)
		try:
			ells_list.append(request.POST['ell-'+id_])
		except:
			pass
	for il in ils:
		id_ = str(il.id)
		try:
			ils_list.append(request.POST['il-'+id_])
		except:
			pass

	if len(jtls_list) == 0:
		vak = Job.objects.filter(draft=True)
	else:
		vak = Job.objects.filter(draft=True).filter(job_type__job_name__in=jtls_list)

	if len(ells_list) == 0:
		vakansiyalar = vak
	else:
		vakansiyalar = vak.filter(job_experience_level__experience_name__in = ells_list)

	if len(ils_list) == 0:
		vakansiyalars = vakansiyalar
	else:
		vakansiyalars = vakansiyalar.filter(job_industry_type__industry_name__in=ils_list)

	try:
		title_ = request.POST['title']
		if not title_ == "":
			vakansiyalars = vakansiyalars.filter(title__icontains=title_)
		else:
			vakansiyalars = vakansiyalars
	except:
		pass
	data['include_'] = render_to_string('job/include.html', {'vakansiyalar': vakansiyalars}, request)
	return JsonResponse(data)

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
