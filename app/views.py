# views.py
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Member
from django.db.models import Q

def home(request):
    return render(request, 'home.html')

@login_required
def index(request):
    query = request.GET.get('q')
    if query:
        mem = Member.objects.filter(Q(name__icontains=query) | Q(subject__icontains=query), user=request.user)
    else:
        mem = Member.objects.filter(user=request.user)
    return render(request, 'index.html', {'mem': mem})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after sign-up
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the main application after sign-in
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

def signout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout

@login_required
def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        country = request.POST['country']
        member = Member(user=request.user, name=name, subject=subject, country=country)
        member.save()
        return redirect('index')
    return render(request, 'add.html')

@login_required
def addrec(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        country = request.POST['country']
        member = Member(user=request.user, name=name, subject=subject, country=country)
        member.save()
        return redirect('index')
    return render(request, 'add.html')

@login_required
def delete(request, id):
    member = Member.objects.get(id=id, user=request.user)
    member.delete()
    return redirect('index')

@login_required
def update(request, id):
    member = Member.objects.get(id=id, user=request.user)
    if request.method == 'POST':
        member.name = request.POST['name']
        member.subject = request.POST['subject']
        member.country = request.POST['country']
        member.save()
        return redirect('index')
    return render(request, 'update.html', {'mem': member})

@login_required
def uprec(request, id):
    if request.method == 'POST':
        member = Member.objects.get(id=id, user=request.user)
        member.name = request.POST['name']
        member.subject = request.POST['subject']
        member.country = request.POST['country']
        member.save()
        return redirect('index')
    return render(request, 'update.html')
