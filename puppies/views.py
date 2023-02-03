from django.shortcuts import render,HttpResponse
from django.urls import include
#import puppies
#from puppies.templates import puppies
# Create your views here.
def index(request):
    return render(request,"pup.html")
    #return HttpResponse("yoyo")

