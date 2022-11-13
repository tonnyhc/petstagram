from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


@login_required
def add_photo(request):
    if request.method == "GET":
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            form.save_m2m()
            return redirect('home-page')
    context = {
        'form': form
    }
    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    likes_count = photo.like_set.all()
    photo_is_liked_by_user = likes_count.filter(user=request.user)
    context = {
        'photo': photo,
        'likes_count': len(likes_count),
        'comment_form': CommentForm(),
        'comments': photo.comment_set.all(),
        'photo_is_liked_by_user': photo_is_liked_by_user
    }
    # TODO: MAKE THIS
    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == "POST":
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('details photo', pk=pk)
    form = PhotoEditForm(instance=photo)
    context = {
        'form': form
    }
    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.like_set.all().delete()
    photo.delete()
    return redirect('home-page')
