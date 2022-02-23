from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# from .forms import SignupForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from tasks.serializers import TasksSerializer, UsersSerializer
from tasks.models import Tasks, Users
import json

@csrf_exempt
def index(request):
    if request.method == "GET":
        snippets = Users.objects.all()
        serializer = UsersSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
        # return render(request,'login.html',{})
    if request.method == "POST":
        # return HttpResponse(request)
        data = JSONParser().parse(request)
        serializer = UsersSerializer(data=data)

        # return HttpResponse(serializer)
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)
        #
# def signup(request):
#     if request.method == "GET":
#         context={}
#         context['signupForm'] = SignupForm()
#         return render(request,'signup.html',context)
#     if request.method == "POST":
#         # login_data = request.POST.dict()
#         # username = login_data.get("name")
#         # password = login_data.get("password")
#         # print(username,password)
#         # return HttpResponse(username,password)
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#         else:
#             signup_form = UserCreationForm()
#             return render(request,'signup.html',{'signup_form':signup_form})
#
#
#
# def changePassword(request):
#     if request.method == "GET":
#         return render(request,'change-password.html',{})
#     if request.method == "POST":
#         return
#