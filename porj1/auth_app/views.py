from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def registerview(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    return render(request,"Auth/register.html",{"form":form})

def loginview(request):
    if request.method == "POST":
        pass
    return render(request,"Auth/login.html",{})