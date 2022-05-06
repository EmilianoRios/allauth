from email import message
from django.shortcuts import redirect, render, HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.

''' NAVBAR - MENU
* LOG IN
* REGISTER  '''

# * LOGIN
def logIn(request):
    return render(request,'loginManager/login.html')

# * REGISTER
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, 'Usuario %s creado' %(username))
            return redirect('/register')
    else:
        form = UserRegisterForm()
    return render(request,'loginManager/register.html',{'form':form})