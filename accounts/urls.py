from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views



app_name="accounts"
urlpatterns = [

    path("login/", views.login_view, name="login"),
    path('cadastro/', views.cadastro_view, name="cadastro"),
    path("logout", views.logout_view, name="logout"),
    path("consulta_email/", views.consulta_email_view, name='consulta_email'),
    #path("solicitar_senha/", views.solicitar_nova_senha, name="solicitar_nova_senha"),
    path("nova_senha/", views.nova_senha, name="nova_senha"),

    path('reset', auth_views.PasswordResetView.as_view(template_name='account/solicitar_senha.html', success_url=reverse_lazy("accounts:password_reset_done")), name="password_reset"),


    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="templates/account/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),


    ]
