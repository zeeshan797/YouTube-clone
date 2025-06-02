from django.shortcuts import render, redirect, get_object_or_404
from .models import Upload
from .forms import UploadForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    # videos = Upload.objects.all()
    users = User.objects.all()
    query = request.GET.get('q')
    if query:
        videos = Upload.objects.filter(title__icontains=query)
    else:
        videos = Upload.objects.all()
    return render(request, 'home.html', {'videos':videos, 'users':users})



@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)  # Don't save yet
            upload.user = request.user         # Assign logged-in user
            upload.save()                      # Now save to DB
            return redirect('home')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})


@login_required
def play(request, id):
    video = get_object_or_404(Upload, id=id)
    video.views+=1
    video.save()
    videos = Upload.objects.exclude(id=id)
    users = User.objects.all()
    return render(request, 'view.html', {'video':video, 'videos':videos, 'users':users})



# Register View
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')  # Change to your home view name
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')  # Change to your home view name
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')  # or 'home'