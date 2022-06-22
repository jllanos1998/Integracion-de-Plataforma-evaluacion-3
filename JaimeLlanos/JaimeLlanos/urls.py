"""JaimeLlanos URL Configuration

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
from django.urls import path
from aplicaciones.apiuser.views import inicio,createUser,editarUser,eliminarUser
from aplicaciones.apiuser.class_view import UserList,UserCreate,UserUpdate,UserDelete,ApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',UserList.as_view(),name='index'),
    path('crearpersona/',UserCreate.as_view(),name="crearpersona"),
    path('editarpersona/<int:pk>',UserUpdate.as_view(),name="editarpersona"),
    path('eliminarpersona/<int:pk>',UserDelete.as_view(),name="eliminarpersona"),
    path('api/',ApiView.as_view(),name="apiget"),
    path('api/<int:id>',ApiView.as_view(),name="apiget")
]
