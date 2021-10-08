from django.urls import path
from . import views
app_name = 'lista'

urlpatterns = [

    path("",  views.index, name='index'),
    path("nova-tarefa/", views.new_tarefa, name='nova-tarefa'),
    path('confirmar/', views.confirmar_item, name='confirmar'),
    path("delete/", views.delete_item, name='delete_item'),


]
