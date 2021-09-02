from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from .models import BlogUser


def registerView(request):
    if request.method == 'GET':
        return render(request, 'registration.html')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return HttpResponse('Passwords does not match')
        user = BlogUser.objects.create_user(username=email, first_name=first_name,
                                            last_name=last_name, age=age, email=email,
                                            password1=password1)
        return HttpResponse('registered')