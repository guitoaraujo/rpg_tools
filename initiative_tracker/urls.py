from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Character URLs
    path('characters/', views.list_characters, name='list_characters'),
    path('character/create/', views.create_or_edit_character, name='create_character'),
    path('character/edit/<int:id>/', views.create_or_edit_character, name='edit_character'),
    path('character/delete/<int:id>/', views.delete_character, name='delete_character'),

    # Encounter URLs
    path('encounter/create/', views.create_encounter, name='create_encounter'),
    path('encounter/<int:id>/', views.encounter_detail, name='encounter_detail'),

    # Change Initiative
    path('change_initiative/<int:id>/', views.change_initiative, name='change_initiative'),
]