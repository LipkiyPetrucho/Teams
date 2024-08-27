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

//account
//GeoNames
$(document).ready(function() {
    $('#id_location').on('input', function() {
        let query = $(this).val();

        // Проверка, что введённый текст не пустой
        if (query.length < 2) {
            $('#suggestions').empty();
            return;
        }

        // Определяем язык
        let lang = 'en';
        if (/[а-яА-ЯЁё]/.test(query)) {
        lang = 'ru';
        }

        // Показать индикацию загрузки
        $('#suggestions').html('<div class="loading">Загрузка...</div>');

        // AJAX запрос к GeoNames API
        $.ajax({
            url: 'http://api.geonames.org/search',
            type: 'GET',
            dataType: 'json',
            data: {
                q: query,
                maxRows: 6, // кол-во результатов
                username: 'petr_lip',
                type: 'json',
                lang: lang,
            },
            success: function(data) {
                $('#suggestions').empty();

                // Функция для создания текста подсказки
                function createSuggestionText(cityData) {
                    const cityName = cityData.name;
                    const countryName = cityData.country || '';  // Если country отсутствует, добавляется пустая строка

                    // Склеиваем название города и страны, если страна доступна
                    return countryName ? `${cityName}, ${countryName}` : cityName;
                }

                // Отображение подсказок
                if (data.geonames && data.geonames.length > 0) {
                    // Сохранение данных в localStorage
                    localStorage.setItem('lastSearchResults', JSON.stringify(data.geonames));

                    data.geonames.forEach(function(city) {
                        const suggestionText = createSuggestionText(city);
                        $('#suggestions').append(`<div class="suggestion" data-name="${city.name}">${suggestionText}</div>`);
                    });


                    // Обработка клика по подсказке
                    $('.suggestion').on('click', function() {
                        $('#id_city').val($(this).data('name'));
                        $('#suggestions').empty();
                    });
                }
            },
            error: function() {
                $('#suggestions').text('Ошибка запроса');
            }
        });
    });
});


