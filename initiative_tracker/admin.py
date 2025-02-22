from django.contrib import admin
from .models.character import Character
from .models.group import Group
from .models.encounter import Encounter

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'initiative')
    search_fields = ('name',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Encounter)
class EncounterAdmin(admin.ModelAdmin):
    list_display = ('id', 'round_number', 'turn_index')
    filter_horizontal = ('characters', 'groups')
