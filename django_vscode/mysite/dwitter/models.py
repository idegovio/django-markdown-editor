from django.db import models
from django.contrib.auth.models import User


# Create a class to define profiles
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #connection to user profile. If deleted, the profile is deleted
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )
    def __str__(self):
        return self.user.username

from django.db.models.signals import post_save
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

# Create a Profile for each new user.
post_save.connect(create_profile, sender=User)




