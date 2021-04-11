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
# import Paper.api_views
# import Paper.views
import curriculum.views
import users.views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('papers/', include('Paper.urls')),
    # path('paper', Paper.views.paper, name='paper'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', curriculum.views.login, name = 'login'),
    path('forms/', curriculum.views.my_form, name = 'forms'),
    path('list/', curriculum.views.index, name = 'list'),
    path('edit/<int:id>', curriculum.views.edit),
    path('update/<int:id>', curriculum.views.update),
    path('delete/<int:id>', curriculum.views.destroy),
    path('', users.views.home, name='home'),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/signup', users.views.SignUp.as_view(), name='signup'),
    path('qna/', include('qna.urls')),


]
