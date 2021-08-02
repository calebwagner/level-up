from django.db import models

class Gamer(models.Model):
    """Gamer Model
    Args:
        models (OneToOneField): The user information for the gamer
        bio (CharField): The bio of the user
    """
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)