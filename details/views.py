from email.policy import default
from sqlite3 import paramstyle
from django.shortcuts import render,HttpResponse

def index(request):
    #return HttpResponse("This is details")
    return render(request,'d1.html')

def ok(request):
    var=request.POST
    params={
        "name":var["name"],
        "breed":var["breed"],
        "date":var["date"]
    }
    print(var)
    return render(request,'s1.html',params)