
function test(){
    $('#btn').click(function(){
        $.ajax('/text/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'test': 'hello'
            },
            'success': function(data){

            }
        })
    })
}

$(document).ready(function{
    test();
})

