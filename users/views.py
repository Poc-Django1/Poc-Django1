from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import CustomRegistrationForm
from .sqs_queue import *
from django.core.mail import send_mail
from django.conf import settings

def home(request):

    return render(request, 'layout.html', {"context": "POC HomePage"})

def welcome(request):
    return render(request, 'welcome.html')

def sqs_queue(user,email):
    message = "Thank you for registering. Register UserID is : " + str(user)
    queuename = "sent_mail"
    create_queue(queuename)
    queue_url = get_queue_url(queuename)
    send_message(queue_url,message)
    receive_data(email)
    
def receive_data(email):
   subject = 'Welcome To online exam portal'
   queue_url = get_queue_url("sent_mail")
   message = receive_message(queue_url)
   print(message)
   email_from = settings.EMAIL_HOST_USER
   recipient = [email,]    
   send_mail( subject, message, email_from, recipient )

class SignUp(generic.CreateView):
    form_class = CustomRegistrationForm
    success_url = reverse_lazy('welcome')
    template_name = 'signup.html'

    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        username, password, email = form.cleaned_data.get('username'), form.cleaned_data.get('password1'), form.cleaned_data.get('email') 
        new_user = authenticate(username=username, password=password)
        sqs_queue(str(username),str(email)) 
        login(self.request, new_user)
        return valid
