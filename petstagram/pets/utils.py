from petstagram.pets.models import Pet


def get_pet_by_slug_and_username(pet_slug, username):
    #TODO: fix when we have auth
    return Pet.objects.get(
        slug=pet_slug,
    )