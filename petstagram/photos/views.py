from django.shortcuts import render, redirect

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
    #TODO: MAKE THIS
    return render(request, 'photos/photo-details-page.html')

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
    photo.delete()
    return redirect('home-page')
