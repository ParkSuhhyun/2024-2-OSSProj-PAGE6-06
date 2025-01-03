from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    username = models.EmailField(unique=True) 
    nickname = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    profileImage = models.CharField(max_length=50, choices=[
        ('image1', 'Image 1'),  # image1은 데이터베이스에 저장되는 값, Image1은 사용자에게 보여주는 표시 이름
        ('image2', 'Image 2'),
        ('image3', 'Image 3'),
        ('image4', 'Image 4')
    ])

    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='custom_user_set',
    #     blank=True,
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='custom_user_permissions_set',
    #     blank=True,
    # )