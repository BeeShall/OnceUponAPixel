$(document).ready(function(){
    var reloader = function(){
        $(".feed-content").html("{% if (LIVE_FEEDS is defined) and LIVE_FEEDS %}{% for content in LIVE_FEEDS %}<div class='feed-entry'><img src='{{content[0]}}' class='img-thumbnail content-image' width='400' height='236'><p>{{content[1]}}</p><hr></div>{% endfor %}{% else %}<br><br><h3 style='color:rgba(240, 0, 0, .6);''>No feed to display.</h3>{% endif %}");
    };


});




