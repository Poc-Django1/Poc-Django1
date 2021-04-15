from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import MyForm
from .models import subjectdetails
from django.contrib import messages

def home(request):
    return render(request, 'layout.html', {"context": "POC HomePage"})

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('list')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def my_form(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = MyForm(request.POST)
            if form.is_valid():
                obj = subjectdetails()
                obj.subject = form.cleaned_data['subject']
                obj.save()
                return redirect('list')
        else:
            form = MyForm()
            return render(request, 'subject.html', {'form': form})

def index(request):
    if request.user.is_authenticated:
      context = {
        'subject': subjectdetails.objects.all(),
      }
      return render(request, 'subject_list.html', context)

def edit(request, id):
    subject = subjectdetails.objects.get(id=id)
    return render(request,'edit.html', {'subject':subject})

def update(request, id):
    subject = subjectdetails.objects.get(id=id)
    form = MyForm(request.POST, instance = subject)
    if form.is_valid():
        form.save()
        return redirect("list")
    return render(request, 'edit.html', {'subject': subject})

def destroy(request, id):
    subject = subjectdetails.objects.get(id=id)
    subject.delete()
    return redirect("list")
