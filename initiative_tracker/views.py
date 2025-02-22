from django.shortcuts import render, get_object_or_404, redirect
from .models import Character, Group, Encounter
from .forms import CharacterForm
from django.http import JsonResponse

# Home page view
def home(request):
    return render(request, 'initiative_tracker/home.html')

# List characters
def list_characters(request):
    characters = Character.objects.all()
    return render(request, 'initiative_tracker/list_characters.html', {'characters': characters})

# Create and edit character
def create_or_edit_character(request, id=None):
    # Se o id for fornecido, estamos editando um personagem existente
    if id:
        character = get_object_or_404(Character, id=id)
    else:
        character = None  # Novo personagem

    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            # Se for um novo personagem, redireciona para a lista de personagens
            return redirect('list_characters')
    else:
        # Se GET ou o formulário for inválido, renderiza a página com os dados
        form = CharacterForm(instance=character)

    return render(request, 'initiative_tracker/create_or_edit_character.html', {'form': form})

# Delete character
def delete_character(request, id):
    character = get_object_or_404(Character, id=id)
    if request.method == 'POST':
        character.delete()
        return redirect('list_characters')
    return render(request, 'initiative_tracker/delete_character.html', {'character': character})

# Create encounter
def create_encounter(request):
    if request.method == 'POST':
        encounter_name = request.POST.get('name')
        encounter = Encounter.objects.create(name=encounter_name)
        return redirect('encounter_detail', pk=encounter.pk)
    return render(request, 'initiative_tracker/create_encounter.html')

# Encounter detail with characters ordered by initiative
def encounter_detail(request, pk):
    encounter = get_object_or_404(Encounter, pk=pk)
    characters = encounter.ordered_characters()

    if request.method == 'POST':
        # Add a character to the encounter
        character_id = request.POST.get('character')
        character = get_object_or_404(Character, pk=character_id)
        encounter.characters.add(character)
        return redirect('encounter_detail', pk=encounter.pk)

    return render(request, 'initiative_tracker/encounter_detail.html', {'encounter': encounter, 'characters': characters})

# Change initiative
def change_initiative(request, pk):
    if request.method == 'POST':
        character = get_object_or_404(Character, pk=pk)
        new_initiative = int(request.POST.get('initiative'))
        character.initiative = new_initiative
        character.save()

        # Reorder characters based on the new initiative
        return JsonResponse({'success': True, 'initiative': character.initiative})
    return JsonResponse({'success': False})
