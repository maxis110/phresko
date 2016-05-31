from restapi.serializers.record_serializer import RecordSerializer
from restapi.models.task import Record
from rest_framework import generics

class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer