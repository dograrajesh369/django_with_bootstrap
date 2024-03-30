from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    context = {
        
    }
    return render(request,'index.html',context)
    # return HttpResponse("this is testing page")

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    return HttpResponse("This is contact page")