
from django.urls import path, include
from Paper import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()

router.register('papers', views.PapersViewSet)


urlpatterns=[
    path('',include(router.urls)),
    path('add_paper/', views.add_paper, name='add-paper'),
    path('list_paper/', views.list_paper, name='list_paper'),
    path('list_paper/update/<int:id>', views.update_paper, name='update_paper'),


]
