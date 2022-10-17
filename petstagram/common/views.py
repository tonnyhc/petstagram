from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.models import Like
from petstagram.photos.models import Photo

def apply_likes_count(photo):
    photo.likes_count = photo.like_set.count()
    return photo

def apply_user_liked_photo(photo):
    #TODO: fix this for current user when authentication is available!!!
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def index(request):

    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos= [apply_user_liked_photo(photo) for photo in photos]
    context = {
        'photos': photos,
    }
    return render(
        request,
        'common/home-page.html',
        context
    )

# def has_user_liked_photo(photo_id):
#     liked_object = Like.objects.filter(to_photo_id=photo_id).first()

def like_photo(request, photo_id):
    #TODO:fix when auth
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    redirect_path = request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
    return redirect(redirect_path)

def share_photo(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('details photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')
