/**
 * Created by josephwon on 12/18/14.
 */
// var etx = {
//     init: function () {
//         etx.callFontFlakes();
//     },
//     callFontFlakes: function(){
//             window.setInterval(function(){
//                         etx.fontFlake();
//             }, 10);
//     },
//     fontFlake: function(){
//         // let set some bloody vars
//         var stageWidth = $(window).width();
//         var stageHeight = $(window).height();
//         var randomEntry = Math.ceil(Math.random()*stageWidth);
//         var preRandomFontSize = Math.ceil(Math.random()*40);
//         var randomFontSize = preRandomFontSize + 10;
//                 var flakeName = 'flake-'+randomEntry;
//                 var grayScale = Math.ceil(Math.random()*256);
//                 var hue = 'rgb('+grayScale+','+grayScale+','+grayScale+ ')';
                
//                 // ok time to create and animate this stupid thing.
//                 $('<div />', {
//                         text: randomEntry,
//                         id: flakeName,
//                 }).appendTo('body').addClass('fontFlake').css('left', randomEntry).css('font-size', randomFontSize).css('color', hue).animate({
//                         "top": "+=" + stageHeight,
//                         opacity: 0
//                 }, 5000, function() {
//                         $('#'+flakeName).remove();                      
//                 }); 
//     }
// };

$(document).ready(function(){
    etx.init();
    $('#title').mouseenter(function(){
        $(this).stop(true, true).fadeTo('fast',0.3);
    });

    $('#title').mouseleave(function(){
        $(this).stop(true, true).fadeTo('fast',1.0);
    });

    

});











