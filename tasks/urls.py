from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get', views.get_tasks, name='get_tasks'),
    path('add', views.add_task, name='add_task'),
    path('del', views.del_tasks, name='del_tasks'),
]
