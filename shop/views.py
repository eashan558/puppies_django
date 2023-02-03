from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from .models import product

# Create your views here.
def index(request):
    # p=product(pname='dove',ptype='soapp',dateadded='2001-11-05')
    # p.save()
    return HttpResponse("your request saved successfully")
    return render(request,"shop.html")

def add(request):
    if request.method=='Post' or request.method=='POST' or request.method=='post' :
        var=request.POST
        p=product(pname=var["pname"],ptype=var["ptype"],dateadded=var["dateadded"])
        p.save()   
    return render(request,'add.html')
