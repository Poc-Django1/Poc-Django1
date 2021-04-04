"""OnlineExamPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import Paper.api_views
import Paper.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('papers/', Paper.api_views.PapersList.as_view(),),
    path('papers/new',Paper.api_views.PapersCreate.as_view()),
    path('papers/<int:id>/', Paper.api_views.PapersRetrieveUpdateDestroy.as_view()),
    path('api/', include('Paper.urls')),
    path('paper', Paper.views.paper, name='paper'),
    path('qna/', include('qna.urls')),
    path('', include('qna.urls')),
]
