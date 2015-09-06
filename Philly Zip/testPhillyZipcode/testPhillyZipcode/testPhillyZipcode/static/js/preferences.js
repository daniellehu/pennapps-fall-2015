function preferencesFunction(status) {
    console.log($(window).innerWidth);
    console.log($(document).innerWidth);
    if ($(window).innerWidth < 992) {
        $(".right-column").HTML('\
                                <p>Parks<input type="range" name="parks" min="0" max="10"></p>\
                    <p>Golf Ranges<input type="range" name="golf" min="0" max="10"></p>\
                    <p>Police Stations<input type="range" name="police" min="0" max="10"></p>\
                    <p>Fire Departments<input type="range" name="fire_department" min="0" max="10"></p>\
                    <p>Litter Index<input type="range" name="litter" min="0" max="10"></p>');
        console.log("less than 992");
    }
    else {
        $(".right-column").HTML('\
                                <p><input type="range" name="parks" min="0" max="10"> Parks</p>\
                    <p><input type="range" name="golf" min="0" max="10"> Golf Ranges</p>\
                    <p><input type="range" name="police" min="0" max="10"> Police Stations</p>\
                    <p><input type="range" name="fire_department" min="0" max="10"> Fire Departments</p>\
                    <p><input type="range" name="litter" min="0" max="10"> Litter Index</p>');
        console.log("more than 992");
    }
    console.log("inside function");
}

$(document).ready(function() {preferencesFunction("docReady")});
$(window).on('resize', function() {preferencesFunction("docResize")});