from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm,EditForm

@login_required
def home(request):
    return render(request,'home.html')



def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        return redirect('login')
    return render(request,'register.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('register')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def todo_list(request):
    tasks=Todo.objects.filter(user=request.user)
    return render(request,'todo_list.html',{'tasks':tasks})

@login_required
def add_task(request):
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
            return redirect('list')
    else:
        form=TodoForm()
    return render(request,'add_task.html',{'form':form})


@login_required
def edit_task(request,pk):
    task=get_object_or_404(Todo,pk=pk,user=request.user)
    if request.method=='POST':
        form=EditForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form=EditForm(instance=task)
    return render(request,'edit_task.html',{'form':form})

@login_required
def delete_task(request,pk):
    task=get_object_or_404(Todo,pk=pk,user=request.user)
    if request.method=='POST':
        task.delete()
        return redirect('list')
    return render(request,'delete_task.html',{'task':task})
