function initialize() {
        var mapCanvas = document.getElementById('map');
        var mapOptions = {
          center: new google.maps.LatLng(39.9500, -75.1667),
          zoom: 8,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        var map = new google.maps.Map(mapCanvas, mapOptions);
        map.data.loadGeoJson("");
        map.data.setStyle({
            fillColor: 'green',
            strokeWeight: 1
        });
      }
google.maps.event.addDomListener(window, 'load', initialize);


