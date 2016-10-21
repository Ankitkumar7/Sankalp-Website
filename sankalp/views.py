from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	context = {
		'name':'sankalp',
	}
	return render(request,'sankalp/index.html',context)
	
