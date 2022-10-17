from django.shortcuts import render

from petstagram.pets.models import Pet
from petstagram.pets.utils import get_pet_by_slug_and_username


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def details_pet(request, username, pet_slug):
    pet = get_pet_by_slug_and_username(pet_slug, username)

    context = {
        'pet': pet,
        'photos_count': pet.photo_set.count(),
        'pet_photos': pet.photo_set.all()
    }

    return render(
        request,
        'pets/pet-details-page.html',
        context
    )


def edit_pet(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')


def delete_pet(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')
