from django.shortcuts import render , HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from Home.models import Contact
from .models import Contact
from django.contrib import messages

def index(request):
    context = {
        'variable1': 'I am a human being',
        'variable2': 'I am not a human being',
    }
    messages.success(request, "This is a success test message!!")
    return render(request, 'index.html', context)
    # return HttpResponse("this is home page")

def About(request):
    return render(request, 'About.html')
    ##return HttpResponse("this is About page")

def service(request):
    return render(request, 'service.html')
    ##return HttpResponse("this is service page")

def ContactView(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
       
        

        if name and email and message:
            contact = Contact(name=name, email=email, message=message)
            contact.save()
            messages.success(request, "your response is recorded")
            return redirect('home')  # or a 'thank you' page
        else:
            return render(request, 'contact.html', {'error': 'All fields are required.'})

    return render(request, 'contact.html')