from django.shortcuts import render, redirect

from petstagram.pets.forms import PetForm, PetDeleteForm
from petstagram.pets.models import Pet
from petstagram.pets.utils import get_pet_by_slug_and_username


def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {
        'form': form
    }
    return render(request, 'pets/pet-add-page.html', context)


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
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "GET":
        form = PetDeleteForm(instance=pet)
    else:
        form = PetDeleteForm(request.POST, instance=pet)
        pet.delete()
        if form.is_valid():
            form.save()
            return redirect('details pet', username, pet_slug)
    context = {
        'form': form,
        'pet_slug':pet_slug,
        'username':username
    }
    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "GET":
        form = PetDeleteForm(instance=pet)
    else:
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            #TODO: fix when auth
            return redirect('profile-details', pk=1)
    context = {
        'form': form
    }
    return render(request, 'pets/pet-delete-page.html', context)
