from django.urls import path, include

from petstagram.accounts import views
from petstagram.accounts.views import show_profile_details, SignUpView, SignInView, \
    SignOutView, EditProfileView, UserDeleteView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', show_profile_details, name='profile-details'),
        path('edit/', EditProfileView.as_view(), name='profile-edit'),
        path('delete/', UserDeleteView.as_view(), name='profile-delete')
    ])),
]
