from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from Paper.serializers import PapersSerializer
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from Paper.models import Papers
from rest_framework.exceptions import ValidationError

class PapersPagination(LimitOffsetPagination):
    default_limit= 10
    max_limit= 100


class PapersList(ListAPIView):
    queryset= Papers.objects.all()
    serializer_class= PapersSerializer
    filter_backends= (DjangoFilterBackend, SearchFilter)
    filter_fields= ('id',)
    search_fields= ('paper_name','subject_id')
    pagination_class= PapersPagination


class PapersCreate(CreateAPIView):
    serializer_class=PapersSerializer
    def create(self, request, *args, **kwargs):

        return super().create(request, *args, **kwargs)


class PapersRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset= Papers.objects.all()
    lookup_field='id'
    serializer_class= PapersSerializer

    def delete(self,request,*args, **kwargs):
        Papers_name= request.data.get('paper_name')
        response= super().delete(request, *args, **kwargs)
        if response.status_code==204:
            from django.core.cache import cache
            cache.delete('Papers_data_{}'.format(Papers_name))
        return response

    def update(self,request, *args, **kwargs):
        response= super().update(request, *args, **kwargs)
        if (response.status_code)==200:
            from django.core.cache import cache
            Papers= response.data
            cache.set('Papers_data_{}'.format(Papers['paper_name']), {
                'paper_desc': Papers['paper_desc'],
                'subject_id': Papers['subject_id'],
                'updated_at': Papers['updated_at'],
            })

            return response
