from django.contrib.auth import login
from django.shortcuts import render, redirect

from account.forms import UserRegisterForm
from account.models import Profile


def view_base(request):
    return render(
        request,
        "base.html",
    )


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Profile.objects.create(user=user)
            return redirect("/")
    else:
        form = UserRegisterForm()
    return render(request, "registration/register.html", {"form": form})
