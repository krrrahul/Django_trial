"""Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from articles.views import HelloTemplate 
from articles import views
from django_test import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
  #  url(r'^hello/$',views.hello,name='hello'),
   # url(r'^hello_template/$',views.hello_template,name='hello_template'),
    #url(r'^hello_template_simple/$',views.hello_template_simple,name='hello_template_simple'),
    #url(r'^hello_class/$',HelloTemplate.as_view(),name='hello_class'),
    url(r'^articles/',include('articles.urls')),
    url(r'^django/',include('django_test.urls')),
]
