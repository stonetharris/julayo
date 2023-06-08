function initMap() {
    const akure = { lat: 7.2534, lng: 5.1931 };
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 13,
      center: akure,
    });
  
    const marker = new google.maps.Marker({
      position: akure,
      map: map,
    });
  }
  