from django.shortcuts import render, get_object_or_404, redirect

def index(request):
	context={}
	context['hello']="Hello world"
	return render(request,'home/home.html',context)
def job_list(request):
	context={}
	return render(request,'job/job-list.html',context)
def job_detail(request):
	context={}
	return render(request,'job/job-detal.html',context)
def about_us(request):
	context={}
	return render(request,'aboutus/aboutus.html',context)