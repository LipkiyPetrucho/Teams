from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from account.forms import UserLoginForm, UserRegisterForm, UserEditForm, ProfileEditForm
from account.models import Profile


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('dashboard')
    redirect_authenticated_user = True

class UserLogoutView(LogoutView):
    next_page = 'login'

@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard',})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user=new_user)
            login(request, new_user)
            return redirect('dashboard')
        else:
            print(form.errors)  # Отладочная информация - вывести ошибки формы
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated ', 'successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User,
                             username=username,
                             is_active=True)
    return render(request,
                  'user/detail.html',
                  {'section': 'people',
                   'user': user})