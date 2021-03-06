// https://docs.djangoproject.com/en/1.7/ref/contrib/csrf/
// https://gist.github.com/rca/1696408
// using jQuery
function getCookie(name)
{
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
 
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
 
$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});

$( document ).ready(function(){

    $('.Switch').click(
        function() {
            if ($(this).hasClass('On')) {
                var dataString =  'state=1'; //Current state is on, so turn off
            }
            else {
                var dataString =  'state=0'; //Current state is off, so turn on
            }
            var urlWithId = "/houseman/" + $(this).attr('id') + "/process/";
            $.ajax
            ({
                type: "POST",
                url: urlWithId,
                data: dataString,
                context: this,
                success: function(){
                    if (dataString == "state=1") {
                        $(this).removeClass("On").addClass("Off");
                    }
                    else {
                        $(this).removeClass("Off").addClass("On");
                    }
                },
            });
        }
    )
});
