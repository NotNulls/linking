from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import SignupForm


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            authenticate(username=user.username, password=user.password)

            if user is not None:
                login(request, user)

                return redirect('/')

    else:
        form = SignupForm()

    return render(request, 'accounts/sign_up.html', {
            'form': form
        })



