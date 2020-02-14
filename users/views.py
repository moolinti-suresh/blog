from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import UserRegister, UserCreation, ProfileForm

# Create your views here.
def register(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    return render(request, 'account/register.html',{'form':form})

@login_required
def profile(request):
    u_form = UserCreation(instance = request.user)
    p_form = ProfileForm(instance = request.user.profile)
    if request.method == 'POST':
        u_form = UserCreation(request.POST, instance = request.user)
        p_form = ProfileForm(request.POST, 
                    request.FILES, 
                    instance = request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    return render(request, 'account/profile.html', {'u_form':u_form, 'p_form':p_form})