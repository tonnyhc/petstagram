from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo


def apply_likes_count(photo):
    photo.likes_count = photo.like_set.count()
    return photo


def apply_user_liked_photo(photo):
    # TODO: fix this for current user when authentication is available!!!
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    comment_form = CommentForm()
    photos = [apply_user_liked_photo(photo) for photo in photos]
    search_form = SearchForm()
    user = request.user
    all_liked_photos_by_request_user = []
    if user.is_authenticated:
        all_liked_photos_by_request_user = [like.to_photo_id for like in user.like_set.all()]
    # TODO: fix the searchBarForm
    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            pass
            # photos = [photo for photo in photos if photo.tagged_pets__name__icontains==search_form.cleaned_data['pet_name']]
            # photos = photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    context = {
        'photos': photos,
        'comment_form': comment_form,
        'search_form': search_form,
        'all_liked_photos_by_request_user': all_liked_photos_by_request_user,
    }
    return render(
        request,
        'common/home-page.html',
        context
    )


# def has_user_liked_photo(photo_id):
#     liked_object = Like.objects.filter(to_photo_id=photo_id).first()
@login_required
def like_photo(request, photo_id):
    # TODO:fix when auth
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id, user=request.user).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo, user=request.user)
        like.save()

    redirect_path = request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
    return redirect(redirect_path)


def share_photo(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('details photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')


def comment_photo(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=photo_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
