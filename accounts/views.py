from django.shortcuts import render, redirect, reverse
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')
    registration_form = RegistrationForm()
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST, request.FILES)
        if registration_form.is_valid():
            user = registration_form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('accounts:dashboard')
    context = {
        'registration_form': registration_form,
    }
    return render(request, 'accounts/register.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')
    login_form = AuthenticationForm()
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:dashboard')
            print(login_form.cleaned_data)
        else:
            login_form.add_error("password", "Invalid Credentials")
            print("Invalid")
    context = {
        'login_form': login_form,
    }
    return render(request, "accounts/login.html", context)

def logout_view(request):
    logout(request)
    return redirect(reverse('core:home'))

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')
