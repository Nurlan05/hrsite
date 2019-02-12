from django.shortcuts import render, get_object_or_404, redirect

def index(request):
	context={}
	context['hello']="Hello world"
	return render(request,'base.html',context)