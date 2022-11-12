from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model

from petstagram.accounts.forms import PetstagramUserCreateForm, SignInForm, PetstagramUserEditForm

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
            'pk':self.object.pk
        })

class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('home-page')

def show_profile_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
