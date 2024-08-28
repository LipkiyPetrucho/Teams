from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404

from games.address_validation import AddressValidator
from games.forms import GameCreateForm
from games.models import Game


@login_required
def game_create(request):
    if request.method == "POST":
        form = GameCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            # Валидируем адрес
            address = cd.get("place")  # предположим, что поле формы для адреса называется place
            city = cd.get("city")
            region_code = 'RU'  # или другая логика получения кода региона

            # Валидируем адрес перед сохранением
            validation_response = address_validator.validate_address(address, region_code, city)

            if 'error' in validation_response:
                messages.error(request, "Ошибка валидации адреса: " + validation_response['error'])
                return render(request, "games/game/create.html", {"section": "games", "form": form})

            new_game = form.save(commit=False)
            new_game.user = request.user
            new_game.save()
            messages.success(request, "Игра успешно создана")
            return redirect(new_game.get_absolute_url())
    else:
        form = GameCreateForm()
    return render(request, "games/game/create.html", {"section": "games", "form": form})


def game_detail(request, id, slug):
    game = get_object_or_404(Game, id=id, slug=slug)
    return render(request,
                  'games/game/detail.html',
                  {'section': 'games',
                   'game': game,
                   })


address_validator = AddressValidator(api_key=settings.GMAPS_KEY)


def validate_address(request):
    if request.method == "POST":
        address = request.POST.get("address")
        # Дополнительные параметры по необходимости
        region_code = request.POST.get("region_code")
        locality = request.POST.get("locality")

        validation_response = address_validator.validate_address(address, region_code, locality)

        if 'error' in validation_response:
            return JsonResponse({"valid": False, "message": validation_response['error']})
        else:
            return JsonResponse({"valid": True, "message": "Address is valid."})
    return JsonResponse({"valid": False, "message": "Invalid request method."})
