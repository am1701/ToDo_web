import {djangoAjax} from "./ajax_django.js";

djangoAjax();



$("#email").on('change', function(){
  var email = $(this).val();

  if ($(this).is(".input-error")){
    $(this).removeClass("input-error")
    $(".btn-cadastro").removeClass("btn-error").text("CADASTRAR").prop('disabled', false);
  }

  if (email != ""){
  $.ajax({
    url : '/c/consulta_email/',
    method : 'POST',
    data : JSON.stringify({email: email }),

    success : function(data){
      if (data.exists) {
        $("#email").addClass("input-error").focus();
        $(".btn-cadastro").addClass('btn-error').text("Email já cadastrado").prop('disabled', true);

      }

    },error : function(xhr){
      console.log('erro')
    }


})

}

})
