from django.shortcuts import render,redirect
from .models import Users, Tasks
from django.http import HttpResponse
from .forms import  SignupForm

# Create your views here.
def index(request):
    context = {'users': Users.objects.all()}
    return render(request,'tasks.html', context=context)
    
def createOrUpdate(request):
    context = {}
    return render(request,'create-tasks.html', context=context)

def delete(request):
    context = {'users':Users.objects.all()}
    return render(request,'tasks.html', context=context)

def signup(request):
    if request.method == "GET":
        context={}
        context['signupForm'] = SignupForm()
        return render(request,'signup.html',context)
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
            return render(request,'signup.html',{'signupForm':form})

        
        
def changePassword(request):
    if request.method == "GET":
        return render(request,'change-password.html',{})
    if request.method == "POST":
        return
      

