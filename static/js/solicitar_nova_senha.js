import {djangoAjax} from "./ajax_django.js";

djangoAjax();

$(".btn-btn").on("click", function (e) {

  e.preventDefault();
  var email = $("#email")

  if (email.val() == "") {
    alert("Preencha o campo email")

  } else {
    $.ajax({
      url : '/c/solicitar_senha/',
      method : 'POST',
      data : JSON.stringify({email: email.val() }),

      success : function(data){
        if(data.exists){
          alertify.set('notifier','position', 'top-center');
          alertify.success('Email Enviado com sucesso! Verifique sua caixa de entrada ou até mesmo o span!');
          email.val("")
        } else {

          alertify.set('notifier','position', 'top-center');
          alertify.error('Email não cadastrado!');

        }
      console.log(data.exists)
      },error : function(xhr){
        console.log('erro')
      }


  })

  }

})
