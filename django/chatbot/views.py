from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
from .forms import InputForm, AddWordForm
from django.contrib.auth import authenticate
# Create your views here.
# Function to get the chatbot response from Flask module
def get_response(request):
    r = requests.get('http://127.0.0.1:5000/response/'+request.GET['msg']) #Sending request to the response module of Flask repo
    data = r.content #Extracting the response from the request object
    return HttpResponse(data.decode('utf-8')) #Sending a status code as response
#Function to render the login form
def login_form(request):
    context = {}
    context['form']= InputForm() #Creating an object of the class InputForm
    return render(request, "login.html", context)
#Function to authenticate admin and render the form to add word
def word_form(request):
    if (request.method == 'POST'):
        username = request.POST['user_name']
        password = request.POST['password']
        #Authenticating admin by matching credentials
        if (username == 'subi' and password == 'Alohomora123'):
            context = {}
            context['form']= AddWordForm() #Creating an object of the AddWordForm class
            return render(request, "addform.html", context)
        else:
            return render(request, "login.html")
#Function to render the chatbot UI
def chatbot(request):
    return render (request, 'chatbot.html', {})
