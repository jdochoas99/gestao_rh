function utilizouHoraExtra(id){
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
    type: 'POST',
    url: 'utilizou_hora_extra' + id + '/',
    data{
        csrfmiddlewaretoken = token
    },
    success:function(result){
        $("#mensagem").text('foi');
    }
    })

    }