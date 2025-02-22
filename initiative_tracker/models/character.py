from django.db import models
from .group import Group

class Character(models.Model):
    player_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    initiative = models.IntegerField(default=0)  # Optional field
    groups = models.ManyToManyField(Group, blank=True)  # Optional field

    def __str__(self):
        return f"{self.name} ({self.initiative})"
