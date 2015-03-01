/**
 * Created by josephwon on 12/18/14.
 */

$(document).ready(function(){
  $('#title').mouseenter(function(){
    $(this).stop(true, true).fadeTo('fast',0.3);
  });

  $('#title').mouseleave(function(){
     $(this).stop(true, true).fadeTo('fast',1.0);
  });

});

//$(document).snow({ SnowImage: "bill.jpg" });





