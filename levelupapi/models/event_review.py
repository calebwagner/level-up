from django.db import models

class EventReview(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """
    review = models.CharField( max_length=1000)
    rating = models.IntegerField()
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
