// Docs at http://simpleweatherjs.com

/* Does your browser support geolocation? */
if ("geolocation" in navigator) {
  $('.js-geolocation').show();
} else {
  $('.js-geolocation').hide();
}

/* Where in the world are you? */
$('.js-geolocation').on('click', function() {
  navigator.geolocation.getCurrentPosition(function(position) {
    loadWeather(position.coords.latitude + ',' + position.coords.longitude); //load weather using your lat/lng coordinates
  });
});

/*
 * Test Locations
 * Austin lat/long: 30.2676,-97.74298
 * Austin WOEID: 2357536
 */
 $.get("http://ipinfo.io", function(response) {
    console.log(response.city, response.country);
$(document).ready(function() {
  loadWeather(response.city, ''); //@params location, woeid
});
}, "jsonp");
function loadWeather(location, woeid) {
  $.simpleWeather({
    location: location,
    woeid: woeid,
    unit: 'f',
    success: function(weather) {
    //'<h2><i class="icon-' +weather.code + '"></i> ' +
      html ='<h2>'+ weather.temp + '&deg;' + weather.units.temp + '</h2>';
      html += '<ul><li>' + weather.city + ', ' + weather.region + '</li>';
      html += '<li class="currently">' + weather.currently + '</li>';
      html += '<li>' + weather.alt.temp + '&deg;C</li></ul>';

      $("#weather").html(html);
    },
    error: function(error) {
      $("#weather").html('<p>' + error + '</p>');
    }
  });
}