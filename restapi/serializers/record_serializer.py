from rest_framework import serializers
from restapi.models.record import Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        field = ('record_id', 'comment', 'record_title', 'create_at', 
        'record_author', 'parent_board', 'record_delete')