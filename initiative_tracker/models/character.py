from django.db import models
from .group import Group

class Character(models.Model):
    player_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    initiative = models.IntegerField(default=0)
    groups = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        return f"{self.name} ({self.initiative})"