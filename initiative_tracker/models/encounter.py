from django.db import models
from .character import Character
from .group import Group

class Encounter(models.Model):
    characters = models.ManyToManyField(Character)
    groups = models.ManyToManyField(Group, blank=True)
    round_number = models.IntegerField(default=1)
    turn_index = models.IntegerField(default=0)

    def next_turn(self):
        self.turn_index += 1
        if self.turn_index >= self.characters.count():
            self.turn_index = 0
            self.round_number += 1
        self.save()

    def __str__(self):
        return f"Encontro {self.id} - Rodada {self.round_number}"

    def ordered_characters(self):
        """Returns the characters ordered by initiative"""
        return self.characters.all().order_by('initiative')
