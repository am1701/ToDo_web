import {djangoAjax} from "./ajax_django.js";

djangoAjax();


$(".btn-cadastro").click(function(e){
  e.preventDefault();
  let nome = $("#nome");
  let email = $("#email");
  let senha = $("#pass");
  var cont = 0;

  $("#form-cadastro input").each(function(){
    if ($(this).val() == ""){
      cont++
    }
  })

  if (cont > 0){
    alertify.set('notifier','position', 'top-center');
    alertify.error('Preencha todos os campos');

  } else if (senha.val().length < 5 ){
    senha.val("").focus()
    alertify.set('notifier','position', 'top-center');
    alertify.error('A senha precisa ter mais de 5 digitos');

  } else {
    $.ajax({
      url : '/c/cadastro/',
      method : 'POST',
      data : JSON.stringify({nome:nome.val(), email: email.val(), senha : senha.val() }),

      success : function(data){
        if (data.created) {
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
