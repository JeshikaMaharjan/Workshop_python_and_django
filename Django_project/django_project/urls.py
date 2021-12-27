"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls), #host.com/admin
    path('search/', TemplateView.as_view(template_name = "hello.html")), #host.com/search (search vanne path ma ayo vane hello.html chai response pathauxa)
    re_path('greet/hari/',TemplateView.as_view(template_name="hi_hari.html")),
    re_path('greet/sita/',TemplateView.as_view(template_name="hi_sita.html")),
    re_path('greet/<name>/',TemplateView.as_view(template_name="hi.html")),
    
]

