from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get', views.tasks, name='get_tasks'),
    path('add', views.add, name='add_task'),
    path('del', views.delete, name='del_tasks'),
]
