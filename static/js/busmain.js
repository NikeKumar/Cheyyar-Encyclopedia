mapboxgl.accessToken =
  "pk.eyJ1IjoibmlrZWt1bWFyIiwiYSI6ImNscTdubHZ0bjE2NTEybG52Z2lxcTJ3OTgifQ.BN0xTCBHzX224qWuDcxPlg"

navigator.geolocation.getCurrentPosition(successLocation, errorLocation, {
  enableHighAccuracy: true
})

function successLocation(position) {
  setupMap([79.5445, 12.6617])
}

function errorLocation() {
  setupMap([79.5418155, 12.6621747])
}

function setupMap(center) {
  const map = new mapboxgl.Map({
    container: "map",
    style: "mapbox://styles/mapbox/streets-v11",
    center: center,
    zoom: 15
  })

  const nav = new mapboxgl.NavigationControl()
  map.addControl(nav)

  var directions = new MapboxDirections({
    accessToken: mapboxgl.accessToken
  })

  map.addControl(directions, "top-left")
}