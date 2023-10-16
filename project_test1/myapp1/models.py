from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, Permission, Group


class CustomUser(AbstractUser):
    # Add custom fields
    age = models.PositiveIntegerField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username

class CustomUser2(AbstractUser):
    # Add custom fields
    age = models.PositiveIntegerField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics2/', blank=True, null=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name="user_set2",
        related_query_name="user2",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="user_set2",
        related_query_name="user2",
    )

    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"