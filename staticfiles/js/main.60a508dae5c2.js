$(document).ready(function(){

  var data = new Date();
  var hora = data.getHours();


  if (hora > 18 ){
    $(".boas_vindas").html('<b>Boa noite</b> ')
  } else if (hora > 12){
    $('.boas_vindas').html("<b>Boa tarde</b> ")
  }else if (hora > 0){
    $(".boas_vindas").html('<b>Bom dia</b> ')
  } else {
    console.log("Bem vindo!")
  }

})
