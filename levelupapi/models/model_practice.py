from django.db import models

class ModelPracticedoesnotmatter(models.Model):
    """Game Model
    Fields:
        models (CharField): The name of the game
        game_type (ForeignKey): The type of game
        description (CharField): The description of the game
        number_of_players (IntegerField): The max number of players of the game
        maker (CharField): The company that made the game
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
