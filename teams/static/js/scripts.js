document.addEventListener("DOMContentLoaded", function() {
    const map = new mapgl.Map('container-gis', {
        key: '2c6f5ef9-bfc1-4fb3-9028-4d0362ee75da',
        center: cityCoordinates,
        zoom: 11,
    });

    if (window.fieldsCoordinates && window.fieldsCoordinates.length > 0) {
        window.fieldsCoordinates.forEach(function(coordinates) {
            const marker = new mapgl.Marker(map, {
                coordinates: coordinates,
            });
        });
    } else {
        console.warn("Нет доступных координат для маркеров.");
    }
});


