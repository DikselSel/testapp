from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from flask import render_template
from . import models
from .forms import NapiszForm

# Create your views here.

def home(request):

    if request.user.is_authenticated:
        redirect('dashboard')


    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request,username=username, password=password)

    try:
        if user is not None:
            login(request,user)
            return redirect('dashboard')
    except:
            return redirect('home')

    

    return render(request, 'home.html')

#Tutaj Jest home
@login_required
def dashboard(request):

    posts = models.TitleScreens.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'dashboard.html', context)



@login_required
def sposoby(request):

    sposoby = models.Sposoby.objects.all()

    context = {
        'sposoby':sposoby,
    }

    return render(request, 'sposoby.html',context)



@login_required
def napisz(request):

    sposoby = models.Sposoby.objects.all()
    stworzone = models.Napisz.objects.all()

    context = {
        'sposoby':sposoby,
        'stworzone': stworzone,
    }

    return render(request, 'napisz.html',context)

@login_required
def napiszCreate(request):

    form = NapiszForm()

    if request.method == 'POST':
        form = NapiszForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('napisz')

    context = {
        'form':form
    }

    return render(request, 'napiszCreate.html', context)

@login_required
def napiszUpdate(request,pk):

    napisz = models.Napisz.objects.get(id=pk)
    form = NapiszForm(instance=napisz)

    if request.method == 'POST':
        form = NapiszForm(request.POST, instance=napisz)
        if form.is_valid():
            form.save()
            return redirect('napisz')

    context = {
        'form': form,
    }

    return render(request,'napiszCreate.html', context)


@login_required
def napiszDelete(request, pk):
    napisz = models.Napisz.objects.get(id=pk)
    if request.method == 'POST':
            napisz.delete()
            return redirect('napisz')

    context = {
        'item':napisz,
    }

    return render(request, 'napiszDelete.html', context)

@login_required
def logout(request):
    logout(request)
    return redirect('home')