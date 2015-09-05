function mainFunction(status) {
    $(".bg").css("height", $(window).innerHeight());   
    console.log($(window).innerHeight());
}


$(document).ready(function() {mainFunction("docReady")});
$(window).on('resize', function() {mainFunction("docResize")});