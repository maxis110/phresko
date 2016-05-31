from restapi.serializers.board_serializer import BoardSerializer
from restapi.models.board import Board
from rest_framework import generics

class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer