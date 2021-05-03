from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ItanikomForm
from .models import Itanikom
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'itanikom/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'itanikom/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)

                return redirect('currentitanikoms')
            except IntegrityError:
                return render(request, 'itanikom/signupuser.html', {'form':UserCreationForm(), 'error': 'That username has already been taken. Please choose a new username'})

        else:
            return render(request, 'itanikom/signupuser.html', {'form':UserCreationForm(), 'error': 'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'itanikom/loginuser.html', {'form':AuthenticationForm()})
    else:
        user =  authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'itanikom/loginuser.html', {'form':AuthenticationForm(), 'error': 'Username and password did not match.'})
        else:
            login(request, user)
            return redirect('currentitanikoms')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def createitanikom(request):
    if request.method == 'GET':
        return render(request, 'itanikom/createitanikom.html', {'form':ItanikomForm()})
    else:
        try:
            form = ItanikomForm(request.POST)
            newitanikom = form.save(commit=False)
            newitanikom.user = request.user
            newitanikom.save()
            return redirect('currentitanikoms')
        except ValueError:
            return render(request, 'itanikom/createitanikom.html', {'form':ItanikomForm(), 'error':'Bad data passed in. Try again'})

@login_required
def currentitanikoms(request):
    itanikoms = Itanikom.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'itanikom/currentitanikoms.html', {'itanikoms':itanikoms})

@login_required
def completeditanikoms(request):
    itanikoms = Itanikom.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'itanikom/completeditanikoms.html', {'itanikoms':itanikoms})

@login_required
def viewitanikom(request, itanikom_pk):
    itanikom = get_object_or_404(Itanikom, pk=itanikom_pk, user=request.user)
    if request.method == 'GET':
        form = ItanikomForm(instance=itanikom)
        return render(request, 'itanikom/viewitanikom.html', {'itanikom':itanikom, 'form':form})
    else:
        try:
            form = ItanikomForm(request.POST, instance=itanikom)
            form.save()
            return redirect('currentitanikoms')
        except ValueError:
            return render(request, 'itanikom/viewitanikom.html', {'itanikom':itanikom, 'form':form, 'error': 'Bad Info'})

@login_required
def completeitanikom(request, itanikom_pk):
    itanikom = get_object_or_404(Itanikom, pk=itanikom_pk, user=request.user)
    if request.method == 'POST':
        itanikom.datecompleted = timezone.now()
        itanikom.save()
        return redirect('currentitanikoms')

@login_required
def deleteitanikom(request, itanikom_pk):
    itanikom = get_object_or_404(Itanikom, pk=itanikom_pk, user=request.user)
    if request.method == 'POST':
        itanikom.datecompleted = timezone.now()
        itanikom.delete()
        return redirect('currentitanikoms')
