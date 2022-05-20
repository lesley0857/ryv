"""ryvm_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from ryvm_app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('pu/<str:id>/', pu_view, name='pu_view'),
    path('ward/<str:id>/', ward_view, name='ward_view'),
    path('pur/<str:id>/', pur_view, name='pur_view'),
    path('tu/<str:id>/', tu_view, name='tu_view')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
