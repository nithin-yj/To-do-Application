from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm,EditForm
from django.core.paginator import Paginator

@login_required
def home(request):
    return render(request,'home.html')



def register(request):
    dict={}
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(username__iexact=username).exists():
            dict['error']='username already exists'
            return render(request,'register.html',dict)
        if username and password and email: 
            user=User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect('login')
        else:
            dict['error']='All 3 fields are required'
            
    return render(request,'register.html',dict)

def login_view(request):
    dict={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            dict['error']='invalid username or password'
    return render(request,'login.html',dict)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def todo_list(request):
    task_list=Todo.objects.filter(user=request.user).order_by('-id')
    paginator=Paginator(task_list,3)
    page_number=request.GET.get('page')
    tasks=paginator.get_page(page_number)
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
