from django.shortcuts import render

# Create your views here.


def home(request):
    return render (request,'home.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    return render(request,'projects.html')

def project_detail(request):
    return render(request,'project_detail.html')
    
