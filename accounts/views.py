from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView

from accounts.forms import LoginForm, RegisterForm


# Create your views here.
# class LoginView(TemplateView):
#     template_name = 'accounts/temps/login.html'
#     form_class = LoginForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = LoginForm
#         return context


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request,
                                    username=cd['username'],
                                    password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('anime_list')
                    else:
                        messages.error(request, 'disabled account')
                        return redirect('login')
            else:
                messages.error(request, 'invalid username or password')
                return redirect('login')
        else:
            form = LoginForm()
        return render(request, 'accounts/temps/login.html', {'form': form})
    return redirect('anime_list')


def register_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                return redirect('anime_list')
            else:
                messages.error(request, 'error password')
        form = RegisterForm()
        return render(request,'accounts/temps/register.html',{'form': form})
    return redirect('login')

@login_required
def logout_view(request):
    if not request.user.is_authenticated:
        logout(request)
    return redirect('anime_list')
