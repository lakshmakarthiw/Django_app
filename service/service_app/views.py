from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index(request):
	list_data = {'name':'django'}
	return render(request,'app/header.html',context=list_data)

