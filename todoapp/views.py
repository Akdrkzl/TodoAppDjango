from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            user_todo = form.save(commit=False)
            user_todo.user = request.user
            user_todo.save()
            return redirect('index')
        else:
            return render(request,'index.html',{'form':form})
    form = TodoForm()
    if request.user.is_authenticated:
        todo = Todo.objects.filter(user = request.user)
    else:
        todo = Todo.objects.all()
    context ={
        'form':form,
        'todo':todo
    }
    return render(request,'index.html',context)

def sil(request):
    if request.method == 'POST':
        id = request.POST['sil']
        sil = Todo.objects.get(id = id)
        sil.delete()
    return redirect('index')