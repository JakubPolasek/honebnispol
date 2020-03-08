"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from prvni.views import majitele_view_post, majitele_view_get, pozemky_view_post, pozemky_view_get
from prvni.views import base_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base_view, name='base'),
    path('', majitele_view_post, name='tab1_post' ),
    path('', majitele_view_get, name='tab1_get' ),
    path('pozemky/', pozemky_view_post, name='tab2_post'),
    path('pozemky/', pozemky_view_get, name='tab2_get'),
]
"""
def my_view(request):
    akce = request.POST.get('novy')
    if akce == '':
        return redirect('/admin/prvni/majitele/add/')
        path('', my_view, name='novy_zaznam'),
"""
