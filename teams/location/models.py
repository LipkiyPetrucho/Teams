from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "city"
        verbose_name_plural = "cities"

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    city = models.ForeignKey(City, related_name="places", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name
