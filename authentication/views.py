from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(self.request, username=user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(self.request, user)
                return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'registration/register.html', context)
