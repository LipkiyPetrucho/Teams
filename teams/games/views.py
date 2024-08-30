from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST

from games.forms import GameCreateForm
from games.models import Game


@login_required
def game_create(request):
    if request.method == "POST":
        form = GameCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
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
    return render(
        request,
        "games/game/detail.html",
        {
            "section": "games",
            "game": game,
        },
    )


@login_required
def game_list(request):
    games = Game.objects.all()
    paginator = Paginator(games, 4)
    page = request.GET.get('page')
    games_only = request.GET.get('games_only')
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        if games_only:
            return HttpResponse('')
        games = paginator.page(paginator.num_pages)
    if games_only:
        return render(request,
                      'games/game/list_games.html',
                      {"section": 'games',
                       'games': games})
    return render(request,
                  'games/game/list.html',
                  {"section": 'games',
                   'games': games})


@login_required
@require_POST
def game_join(request):
    game_id = request.POST.get('id')
    # action берется из атрибута action="/submit", если его нет, то есть ещё варианты.
    action = request.POST.get('action')
    if game_id and action:
        try:
            game = Game.objects.get(id=game_id)
            if action == 'join':
                if game.joined_players.count() >= game.max_players:
                    messages.error(request,
                                     'Максимальное количество игроков достигнуто.')
                    return JsonResponse({'status': 'error',
                                         'message': 'Максимальное количество игроков достигнуто.'})
                game.joined_players.add(request.user)
            else:
                game.joined_players.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Game.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})