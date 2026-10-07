from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome to the task management system.")
def contact(request):
    return HttpResponse("<i>This is the contact page</i>")
def show_task(request):
    return HttpResponse("This is the show_task page")
