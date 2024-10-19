from django.shortcuts import render, redirect  
from .models import Crud
from .forms import CrudForm
from datetime import datetime
# Create your views here.  
def reg(request):  
    if request.method == "POST":  
        form = CrudForm(request.POST) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = CrudForm() 
    return render(request,'index.html',{'form':form})  
def show(request):  
    objects = Crud.objects.all()  
    return render(request,"show.html",{'objects':objects})  
def edit(request, id):  
    object = Crud.objects.get(id=id)  
    return render(request,'edit.html', {'object':object})  
def update(request, id):  
    object = Crud.objects.get(id=id)  
    form = CrudForm(request.POST, instance = object) 
    if form.is_valid(): 
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'object':object})  
def destroy(request, id):  
    object = Crud.objects.get(id=id)
    object.delete()  
    return redirect("/show")  