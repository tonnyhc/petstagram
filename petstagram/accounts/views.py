from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model

from petstagram.accounts.forms import PetstagramUserCreateForm, SignInForm, PetstagramUserEditForm
from petstagram.pets.models import Pet

UserModel = get_user_model()


class SignUpView(views.CreateView):
    model = UserModel
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home-page')


class SignInView(auth_views.LoginView):
    form_class = SignInForm
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('home-page')


class EditProfileView(views.UpdateView):
    model = UserModel
    form_class = PetstagramUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={
            'pk': self.object.pk
        })


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('home-page')


class UserDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'
    next_page = reverse_lazy('home-page')

    def post(self, *args, pk):
        self.request.user.delete()


class ProfileDetailsView(views.DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['pets_count'] = self.object.pet_set.count()

        photos = self.object.photo_set \
            .prefetch_related('like_set')

        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.like_set.count() for x in photos)
        context['pets'] = self.object.pet_set.all()

        return context