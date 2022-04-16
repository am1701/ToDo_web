


$(".btn-revel").click(function(e){
  e.preventDefault();

  var tipo_texto = $("#pass").is('input[type="text"]')
  var tipo_senha = $("#pass").is('input[type="password"]')

  if (tipo_texto){
    $("#pass").prop("type", "password").focus()
    $(".btn-revel").text("Revelar")
  } else {
    $("#pass").prop("type", "text").focus()
    $(".btn-revel").text("Esconder")
  }
})


$("#pass").on("focus", function (){
  $(".btn-revel").css({"display":"block"})
})
