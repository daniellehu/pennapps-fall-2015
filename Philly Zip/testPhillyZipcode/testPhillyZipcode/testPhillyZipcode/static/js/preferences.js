function preferencesFunction(status) {
    if ($(window).innerWidth() < 992) {
        
        $(".right-column").html('\
                                <p>Parks<input type="range" name="parks" min="0" max="10"></p>\
                    <p>Golf Ranges<input type="range" name="golf" min="0" max="10"></p>\
                    <p>Police Stations<input type="range" name="police" min="0" max="10"></p>\
                    <p>Fire Departments<input type="range" name="fire_department" min="0" max="10"></p>\
                    <p>Litter Index<input type="range" name="litter" min="0" max="10"></p>');
    }
    else {
        $(".right-column").html('\
                                <p><input type="range" name="parks" min="0" max="10"> Parks</p>\
                    <p><input type="range" name="golf" min="0" max="10"> Golf Ranges</p>\
                    <p><input type="range" name="police" min="0" max="10"> Police Stations</p>\
                    <p><input type="range" name="fire_department" min="0" max="10"> Fire Departments</p>\
                    <p><input type="range" name="litter" min="0" max="10"> Litter Index</p>');
    }
}

$(document).ready(function() {preferencesFunction("docReady")});
$(window).on('resize', function() {preferencesFunction("docResize")});