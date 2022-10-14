from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to the project</h1>")
def home(request):
    return HttpResponse("<h1>Welcome to homepage</h1>")
def hiname(request,name):
    return HttpResponse("<h1>Hello {}</h1>".format(name))
def add(request,a,b):
    return HttpResponse("<h1>Sum of {} and {} is {}</h1>".format(a,b,int(a)+int(b)))
def tempdemo(request):
   fruits=['apple','banana','mango','chikku','dragon fruit']
   return render(request,'template1.html',context={'name':'shreyas','fruits':fruits}) 
def grt2(request,a,b):
   return render(request,'template2.html',context={'a':a,'b':b})
def hometemp(request):
    return render(request,'Pages/home.html')
def abouttemp(request):
    return render(request,'Pages/about.html')
def register(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        gender=request.POST.get("gender")
        worktype=request.POST.get("worktype")
        skills=request.POST.getlist("skills")
        if request.FILES:
            file=request.FILES['profilepic']
            fs=FileSystemStorage()
            saved_file=fs.save(file.name,file)
            file_url=fs.url(saved_file)
        return HttpResponse("<h1>Success</h1>")
    return render(request,'Pages/register.html')
