from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import User
from django.contrib.auth import login as login_j, authenticate
from django.contrib.auth import logout

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError

def login_view(request):
    template_name = "account/login.html"

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        req = json.load(request)
        email = req["email"]
        senha = req["senha"]

        try:
            user =  User.objects.get(email__iexact=email)
            if user and user.is_active and user.check_password(senha):
                usuario = authenticate(request, username=email, password=senha)
                login_j(request, usuario)
                data = {'logado': True}
                return JsonResponse(data)
            else:
                print('Usuário ou senha invalidos')
                data = {'invalid': True}
                return JsonResponse(data)
        except User.DoesNotExist:
            data = {'invalid': True}
            return JsonResponse(data)

    return render(request, template_name)



def cadastro_view(request):
    template_name = "account/signup.html"

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        sobrenome = "not"
        req = json.load(request)
        email = req["email"]
        senha = req["senha"]
        nome = req["nome"].split(" ")
        if len(nome)>1:
            sobrenome=nome[1]
        print(f"nome {nome} | sobrenome {sobrenome}")
        User.objects.create_user(username=email, email=email, password=senha, first_name=nome[0], last_name=sobrenome)
        usuario = authenticate(request, username=email, password=senha)
        login_j(request, usuario)
        data = {'created': True}
        return JsonResponse(data)

    return render(request, template_name)



def logout_view(request):
    logout(request)
    return redirect('lista:index')


def consulta_email_view(request):

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            req = json.load(request)
            email = req["email"]
            user = User.objects.get(email__iexact=email)
            if user:
                data = {'exists':True}
                return JsonResponse(data)
        except User.DoesNotExist:
            data = {'exists':False}
            return JsonResponse(data)



def solicitar_nova_senha(request):

    ...
    '''
    template_name = "account/solicitar_senha.html"

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            req = json.load(request)
            email = req['email']
            user = User.objects.get(email__iexact=email)
            if user:
                assunto = 'Recupere sua senha'
                email_template_name = "account/template_email.txt"

                c = {
                'email' : user.email,
                'dominio' : '127.0.0.1:8000',
                'site_name' : "ToDoListWeb",
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                'user' : user,
                'token' : default_token_generator.make_token(user),
                'protocolo': 'http'
                }
                email = render_to_string(email_template_name, c)

                try:
                    send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect("accounts:password_reset_complete")

        except User.DoesNotExist:
            data = {'exists' : False}
            return JsonResponse(data)

    return render(request, template_name)
'''

def nova_senha(request):
    template_name = "account/new_senha.html"

    return render(request, template_name)
