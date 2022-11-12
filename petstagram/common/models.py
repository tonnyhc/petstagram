from django.contrib.auth import get_user_model
from django.db import models

from petstagram.photos.models import Photo

UserModel = get_user_model()

class Comment(models.Model):
    comment_text = models.TextField(
        max_length= 300
    )
    date_and_time_of_publication = models.DateField(
        auto_now= True
    )
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(
        to=UserModel,
        on_delete= models.CASCADE
    )

    class Meta:
        ordering = ['-date_and_time_of_publication']

class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null = False,
        blank = True
    )
    user = models.ForeignKey(
        to=UserModel,
        on_delete= models.CASCADE
    )