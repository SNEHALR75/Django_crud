from django.shortcuts import render,redirect
from .models import Food
from .forms import FoodModelForm
# Create your views here.

def addview(request):
    form = FoodModelForm()
    if request.method == "POST":
        form = FoodModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/show/")
    return render(request,"app1/add.html",{"form":form})

def showview(request):
    obj = Food.objects.all()
    return render(request,"app1/show.html",{"obj":obj})

def updateview(request,i):
    f = Food.objects.get(id=i)
    form = FoodModelForm(instance=f)
    if request.method == "POST":
        form = FoodModelForm(request.POST,instance=f)
        if form.is_valid():
            form.save()
            return redirect("/show/")
    return render(request, "app1/add.html", {"form":form})

def deleteview(request,i):
    f1 = Food.objects.get(id=i)
    if request.method == "POST":
        f1.delete()
        return redirect("/show/")
    return render(request,"app1/delete.html",{"f1":f1})