from levelupapi.models.model_practice import ModelPracticedoesnotmatter
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from levelupapi.models import ModelPracticedoesnotmatter


class PracticeView(ViewSet):

    def list(self, request):

        practiceFixture = ModelPracticedoesnotmatter.objects.all()

        serializer = PracticeSerializer(
            practiceFixture, many=True, context={'request': request})
        return Response(serializer.data)


class PracticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelPracticedoesnotmatter
        fields = '__all__'
        depth = 1