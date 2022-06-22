
from django.contrib import admin
from django.urls import path
from aplicaciones.apiuser.views import UserList,UserCreate,UserUpdate,UserDelete,ApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',UserList.as_view(),name='index'),
    path('crearpersona/',UserCreate.as_view(),name="crearpersona"),
    path('editarpersona/<int:pk>',UserUpdate.as_view(),name="editarpersona"),
    path('eliminarpersona/<int:pk>',UserDelete.as_view(),name="eliminarpersona"),
    path('api/',ApiView.as_view(),name="apiget"),
    path('api/<int:id>',ApiView.as_view(),name="apiget")
]
