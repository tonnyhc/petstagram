from django.contrib import admin

from petstagram.common.models import Comment, Like
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'get_tagged_pets')

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join([pet.name for pet in obj.tagged_pets.all()])

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass