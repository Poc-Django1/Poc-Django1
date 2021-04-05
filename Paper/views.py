from django.shortcuts import render
from rest_framework import status,viewsets
from Paper.models import Papers
from Paper.serializers import PapersSerializer
from django.http import HttpResponseRedirect
from .forms import PaperForm
from django.template.context import RequestContext




# Create your views here.
def paper(request):
    return render(request, 'paper.html')

class PapersViewSet(viewsets.ModelViewSet):
    serializer_class= PapersSerializer
    queryset=Papers.objects.all()


def add_paper(request):
     submitted = False
     if request.method == 'POST':
         form = PaperForm(request.POST)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect('?submitted=True')
     else:
         form = PaperForm()
         if 'submitted' in request.GET:
             submitted = True
     return render(request,
         'add_paper.html',
         {'form': form, 'submitted': submitted},
     )



def list_paper(request):
    context ={}

    # add the dictionary during initialization
    paperlist = Papers.objects.all()
    return render(request, 'list_paper.html', {'paperlist': paperlist})


def update_paper(request, id):
    updated = False
    paper_id = int(id)
    try:
        paper_sel = Papers.objects.get(id = paper_id)
    except Papers.DoesNotExist:
        return redirect('add_paper')
    paper_form = PaperForm(request.POST or None, instance = paper_sel)
    if paper_form.is_valid():
       paper_form.save()
       return HttpResponseRedirect('?updated=True')
#
    if 'updated' in request.GET:
        updated = True
        return render(request,
            'add_paper.html',
            {'updated': updated,'update_paper':paper_form},
     )

    else:
        return render(request, 'update_paper.html', {'update_paper':paper_form})


def delete_paper(request, id):
    deleted = False
    paper_id = int(id)
    paperlist = Papers.objects.all()

    try:
        paper_sel = Papers.objects.get(id = paper_id)
        #paper_sel.delete()
    #except Papers.DoesNotExist:
    except Exception as e:
        print (e)
        return render(request, 'list_paper.html', {'paperlist': paperlist})

    paper_sel.delete()
    print (e)
    return HttpResponseRedirect('?deleted=True')
    if 'deleted' in request.GET:
        deleted = True
        return render(request,
            'add_paper.html',
            {'deleted': deleted},
     )

    else:
        return render(request, 'add_paper.html')
