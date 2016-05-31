from rest_framework import serializers
from restapi.models.task import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        field = ('task_id', 'task_name')