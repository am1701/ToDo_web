from django.shortcuts import render
from .models import Lista
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .utils import send_email

import json

def index(request):

    template_name = 'lista/index.html'
    contexto = {}

    return render (request, template_name, contexto)



@login_required
def new_tarefa(request):
    template_name = 'lista/novo.html'
    item = Lista.objects.filter(usuario=request.user)
    if request.method == 'POST' and request.is_ajax():
        items = json.load(request)
        msg = items['texto']
        iditem = Lista.objects.create(item=msg, usuario=request.user).id

        data = {'msg':msg, 'ok_add': True, 'iditem':iditem}
        return JsonResponse(data)

    tarefas = Lista.objects.filter(usuario=request.user)


    contexto = {'tarefas':tarefas}
    

    return render (request, template_name, contexto)

def confirmar_item(request):
    if request.method == 'POST' and request.is_ajax():
        id_item = json.load(request)['data']

        item = Lista.objects.get(id=id_item)
        if item.usuario == request.user:
            if item.feito:
                item.feito = False
                item.save()
                data = {'item': False}
            else:
                item.feito = True
                item.save()
                data = {'item': True}
        return JsonResponse(data)


def delete_item(request):
    if request.method == 'POST' and request.is_ajax():
        id_item = json.load(request)['data']
        item = Lista.objects.filter(usuario=request.user).filter(id=id_item)
        if item:
            item.delete()
            data = {'deleted':True}
        else:
            data = {'deleted': False}

        return JsonResponse(data)
