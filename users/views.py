from django.shortcuts import render , redirect
from  django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_name =form.cleaned_data.get('username')
            messages.success(request, f"Welcome {user_name }, you have been successfully registered")
            return redirect('users:login')
    form = RegisterForm()
    context ={
        'form': form
    }
    return render(request,'users/register.html', context)


def logout_view(request):
  
    logout(request)

    return render(request, 'users/logout.html')

@login_required
def profile(request):
    return render(request,'users/profile.html')
