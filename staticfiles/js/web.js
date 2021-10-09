$(document).ready(function(){

$(".new-btn").on('click', function(){

  var texto = $('.add-task').val();
  var data_item = $('#datetimepicker').val();

  let url = "/nova-tarefa/"

  if (texto === '' || data_item === '' ){
    alert('Digite o item e data')
  } else {


    $.ajax({
      url : url,
      method : "POST",
      data : JSON.stringify({texto: texto, data_item:data_item}),
      success : function(data){
        if(data.ok_add){
          $('.add-task').val("");
          $('#datetimepicker').val("")
          console.log(data_item);
          var add_dados = `
            <div class="false">
              <div class="id_item" style='display:none;'>${data.iditem}</div>
              <div class="texto"><i class="far fa-circle no-checked mr-2"></i> ${data.msg} <i class="fas fa-trash-alt icon"></i></div>
              <span class="data_hora">${data.data} - ${data.hora}</span>
            </div>
            `
          $(".fundo").append(add_dados);
        }
      },
      error : function(xhr){
        console.log('erro')
      },
      complete: function() {


      }
    });
    //fim ajax
 }
})

var confirmar_item = function (id, item){
  var id_item = id
  var _item = item
  $.ajax({
    url : '/confirmar/',
    method : 'POST',
    data : JSON.stringify({data: id_item}),
    success : function(data) {
      if (data.item){
        $(item).removeClass('false').addClass("true")
        $(item).children('.texto').children(".no-checked").removeClass('far fa-circle no-checked mr-2').addClass("fas fa-check-circle checked mr-2")
      } else {
        $(item).removeClass('true').addClass("false")
        $(item).children('.texto').children(".checked").removeClass('fas fa-check-circle checked mr-2').addClass("far fa-circle no-checked mr-2")
      }
    }, error : function(xhr){
      console.log('erro')
    },
  })


}

var deletar_item = function(id, item){
  var id_item = id
  var _item = item
  $.ajax({
    url : '/delete/',
    method : 'POST',
    data : JSON.stringify({data: id_item}),
    success : function (data){
      if (data.deleted){
          $(item).remove();
          
      }
    },
    error : function(xhr) {
      console.log("Error")
    },

  })

}

$(document).on('click','.true',  function (e){

  var xPosition=e.pageX;
  var id_item = $(this).children('.id_item').text()
  var item = $(this)

  if(xPosition>01 && xPosition<1050){
    confirmar_item(id_item, item);
  } else {
    deletar_item(id_item, item)
  }
  })

//função que confirma item como feito
$(document).on('click', '.false', function (e){

  var xPosition=e.pageX;
  var id_item = $(this).children('.id_item').text()
  var item = $(this)

  if(xPosition>01 && xPosition<1050){
    confirmar_item(id_item, item);
  } else {
    deletar_item(id_item, item)
  }

})

$('.add-task').keypress(function(event){
  if(event.keyCode === 13){
    $(".new-btn").click();
  }
})




$(document).keydown(function(event){
    var input = $('.add-task')
    if (event.keyCode === 46 && !input.is(':focus')){
    $(".id_item").css('display', 'block');
  }else if (event.keyCode === 78 && !input.is(':focus')){
    $('.add-task').focus();
  }
})

/*document.addEventListener("keydown", function(event) {
    var input = $('.add-task').is(':focus')
    if (event.keyCode === 46 && !input){
      $(".id_item").css('display', 'block');
    } else if (event.keyCode === 78 && !input){
      $('.add-task').focus();
      $('.add-task').reset()
    }

})*/
//ajax django
var getCookie = function (name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

var csrfSafeMethod = function (method) {
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
  }
});


})
