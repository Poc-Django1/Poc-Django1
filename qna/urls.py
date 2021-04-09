from django.urls import path, re_path
from . import views
from django.contrib import admin

urlpatterns = [
    path('',views.show),
    path('addqna',views.addqna),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]


