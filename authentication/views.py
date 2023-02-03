from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    var=request.POST
    if "loginid" and "password" in var.keys():
        if var["loginid"]=="eashan" and var["password"]=="sarkar" :
            return HttpResponse("You are logged in")
        else:
            params={"alert":"Invalid Credentials Entered!!! Try Again"}
            return render(request,'login.html',params)
    else:
        #return HttpResponse("Wrong details")
        return render(request,'login.html')

def forgot(request):
    return render(request,'forgot.html')

def check(request):
    var=request.POST 
    if var["loginid"]=="eashan" and var["password"]=="sarkar" :
        return HttpResponse("You are logged in")
    else:
        return HttpResponse("Wrong details")