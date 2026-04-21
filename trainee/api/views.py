from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from trainee.models import Trainee

from .serializers import TraineeSerializer


@api_view(["GET"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def trainee_list(request):
    # Read-only endpoint for listing all trainees.
    trainees = Trainee.objects.all()
    serializer = TraineeSerializer(trainees, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def trainee_detail(request, id):
    # Read-only endpoint for retrieving one trainee by id.
    trainee = get_object_or_404(Trainee, id=id)
    serializer = TraineeSerializer(trainee)
    return Response(serializer.data, status=status.HTTP_200_OK)


class TraineeCreateAPIView(generics.CreateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class TraineeUpdateAPIView(generics.UpdateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
    lookup_field = "id"
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class TraineeDestroyAPIView(generics.DestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer
    lookup_field = "id"
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
