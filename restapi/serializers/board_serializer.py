from rest_framework import serializers
from restapi.models.board import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        field = ('board_id', 'board_title', 'board_author', 'board_delete')