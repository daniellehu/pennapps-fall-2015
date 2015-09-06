function preferencesFunction(status) {
    if ($(window).innerWidth() < 992) {
        
        $(".right-column").html('\
                                <h3><p class="hover-off">Number of parks that are accessible to the public.</p>\
                    Parks <input type="range" name="parks" min="0" max="10"></h3>\
                    <h3><p class="hover-off">Number of golf courses nearby.</p>\
                        Golf Ranges  <input type="range" name="parks" min="0" max="10"></h3>\
                    <h3><p class="hover-off">Quantities the number of police precincts in the  \
area.</p> Police Stations <input type="range" name="police" min="0" max="10"></h3>\
                    <h3><p class="hover-off">Number of fire department facilities in close  \
proximity.</p> Fire Departments<input type="range" name="police" min="0" max="10"></h3>\
                    <h3><p class="hover-off">Prevalence of litter within the surrounding area.</p>\
                                Litter Index <input type="range" name="police" min="0" max="10"></h3>');
    }
    else {
        $(".right-column").html('\
                                <h3><p class="hover-off">Number of parks that are accessible to the public.</p>\
                        <input type="range" name="parks" min="0" max="10"> Parks</h3>\
                    <h3><p class="hover-off">Number of golf courses nearby.</p>\
                        <input type="range" name="golf" min="0" max="10"> Golf Ranges</h3>\
                    <h3><p class="hover-off">Quantities the number of police precincts in the  \
area.</p>\
                        <input type="range" name="police" min="0" max="10"> Police Stations</h3>\
                    <h3><p class="hover-off">Number of fire department facilities in close  \
proximity.</p>\
                        <input type="range" name="fire_department" min="0" max="10"> Fire Departments</h3>\
                    <h3><p class="hover-off">Prevalence of litter within the surrounding area.</p>\
                        <input type="range" name="litter" min="0" max="10"> Litter Index</h3>');
    }
    if (status == "docReady") {
        $("h3").mouseenter(function() {
            $(this).children(".hover-off").addClass("hover-on");
        });
        $("h3").mouseleave(function() {
            $(this).children(".hover-off").removeClass("hover-on");
        });
    }
}

$(document).ready(function() {preferencesFunction("docReady")});
$(window).on('resize', function() {preferencesFunction("docResize")});