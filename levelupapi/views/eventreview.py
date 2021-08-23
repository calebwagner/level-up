"""View module for handling requests about games"""
from levelupapi.models.event import Event
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from levelupapi.models import EventReview
from django.contrib.auth.models import User


class EventReviewView(ViewSet):
    """[summary]

    Args:
        ViewSet ([type]): [description]
    """
    def create(self, request):
        """[summary]

        Args:
            request ([type]): [description]

        Returns:
            [type]: [description]
        """
        review = EventReview()
        review.review = request.data["review"]
        review.rating = request.data["rating"]
        review.event = request.data["event"]

        event = Event.objects.get(pk=request.data["game_id"])
        review.event = event

        review.player = request.auth.user
     
        try:
            review.save()
            serializer = ReviewSerializer(review, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


    def list(self, request):
        """Handle GET requests to review resource
        Returns:
            Response -- JSON serialized list of categories
        """
        reviews = EventReview.objects.all()

        serializer = ReviewSerializer(
            reviews, many=True, context={'request': request})
        return Response(serializer.data)

    # def update(self, request, pk=None):
    #     """Handle PUT requests for an event
    #     Returns:
    #         Response -- Empty body with 204 status code
    #     """
    #     gamer = EventReview.objects.get(user=request.auth.user)

    #     review = Event()
    #     review.review = request.data["review"]
    #     review.rating = request.data["rating"]
    #     review.event = request.data["event"]

    #     game = Game.objects.get(pk=request.data["game"])
    #     event.game = game
    #     event.save()

    #     return Response({}, status=status.HTTP_204_NO_CONTENT)

class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews
    Arguments:
        serializer type
    """
    class Meta:
        model = EventReview
        fields = '__all__'
        depth = 1