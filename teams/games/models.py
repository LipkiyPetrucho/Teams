from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Game(models.Model):
    SPORTS = (
        ("football", "футбол"),
        ("tennis", "теннис"),
        ("bowling", "боулинг"),
        ("beach volleyball", "пляжный волейбол"),
        ("volleyball", "волейбол"),
        ("ice hockey", "хоккей на льду"),
        ("chess", "шахматы"),
    )
    SPORT_ICONS = {
        "football": "football-icon.png",
        "tennis": "tennis-icon.png",
        "ice hockey": "hockey-icon.png",
    }

    CHOICES = (("open", "Open"), ("started", "Started"), ("finished", "Finished"))

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="user_games_created",
        on_delete=models.CASCADE,
    )
    sport = models.CharField(max_length=255, choices=SPORTS)
    city = models.CharField(max_length=100, default="Самара")
    place = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default=timezone.now)
    duration = models.DurationField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    max_players = models.PositiveIntegerField(default=2)
    joined_players = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="joined_games", blank=True
    )
    status = models.CharField(max_length=255, choices=CHOICES, default="Open")
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
        indexes = [
            models.Index(fields=["created_at"]),
        ]
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.sport} {self.date} {self.start_time} {self.place}"

    def save(self, *args, **kwargs):
        """
        Если слаг не задан, генерирует его из названия вида спорта, даты и места.
        """
        if not self.slug:
            self.slug = (
                slugify(self.sport, allow_unicode=True)
                + "-"
                + slugify(self.date, allow_unicode=True)
                + "-"
                + slugify(self.created_at, allow_unicode=True)
                + "-"
                + slugify(self.user, allow_unicode=True)
            )
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("games:detail", args=[self.id, self.slug])
