from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home-page')
    context = {
        'form':form
    }
    return render(request, 'photos/photo-add-page.html', context)

def details_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    likes_count = photo.like_set.all()
    context = {
        'photo':photo,
        'likes_count': len(likes_count),
        'comment_form': CommentForm(),
        'comments': photo.comment_set.all()
    }
    #TODO: MAKE THIS
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
        'form':form
    }
    return render(request, 'photos/photo-edit-page.html',context)

def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.like_set.all().delete()
    photo.delete()
    return redirect('home-page')
