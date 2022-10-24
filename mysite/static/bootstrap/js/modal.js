var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

$(document).ready(function(){
        $("#exampleModal").modal();
        });


$('#NewsView').on('show.bs.modal', function (event) {
            // получить кнопку, которая его открыло
            var button = $(event.relatedTarget)
            // извлечь информацию из атрибута data-content
            var content = button.data('content')
            // вывести эту информацию в элемент, имеющий id="content"
            $(this).find('#content').text(content);
        });