from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import CustomRegistrationForm


def home(request):

    return render(request, 'home.html', {"context": "POC HomePage"})


class SignUp(generic.CreateView):
    form_class = CustomRegistrationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid
