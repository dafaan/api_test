from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        mail = request.POST['email']
        check_mail = User.objects.filter(email=mail)
        print(check_mail)
        if len(check_mail) >= 1:
            messages.info(request, 'email taken')
            print('mail taken')
            return redirect('register')
            
        else:
            print('good mail')
            messages.info(request, 'clean mail')
            user = User.objects.create_user(username=firstname, last_name=lastname, password=password, email=mail)
            user.save()
            return redirect('/')
    return render(request, 'register.html')