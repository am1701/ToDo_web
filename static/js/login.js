import {djangoAjax} from "./ajax_django.js";

djangoAjax();



$(".btn-login").on("click", function (e){
var cont = 0;
  e.preventDefault();

  $("#form-login input").each(function (){
    if ($(this).val() == ''){
      cont++
    }
  })

  var email = $("#user")
  var senha = $("#pass")


    if (cont > 0){
      alertify.set('notifier','position', 'top-center');
      alertify.error('Preencha todos os campos');

    } else {

      $.ajax({
        url : '/c/login/',
        method : 'POST',
        data : JSON.stringify({email: email.val(), senha : senha.val() }),

        success : function(data){
          if (data.logado) {
              window.location = '/nova-tarefa/'
          } else {
            senha.val("").focus()
            alertify.set('notifier','position', 'top-center');
            alertify.error('Email ou senha incorretos.');

          }

        },error : function(xhr){
          console.log('erro')
        }


    })
  }
})
