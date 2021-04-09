from django.http import HttpResponse
from qna.forms import QnaForm
from qna.models import Questionanswers
from django.shortcuts import render, redirect



def addqna(request):

    if request.method == "POST":
        form = QnaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/qna/show')
            except Exception as e:
                pass
    else:
        form = QnaForm()
    return render(request,'index.html',{'form':form})

def show(request):
    qnas = Questionanswers.objects.all()
    return render(request,"show.html",{'qnas':qnas})

def edit(request, id):

    qnas = Questionanswers.objects.get(id=id)
    return render(request,'edit-qna.html', {'qnas':qnas})

def update(request, id):
    qnas = Questionanswers.objects.get(id=id)
    form = QnaForm(request.POST, instance = qnas)
    if form.is_valid():
        form.save()
        return redirect("/qna/show")
    return render(request, 'edit.html', {'employee': qnas})

def destroy(request, id):
    qna = Questionanswers.objects.get(id=id)
    qna.delete()
    return redirect("/qna/show")
