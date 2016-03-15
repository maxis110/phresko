from rest_framework import serializers
from models import User, Category, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_name', 'email')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = ('category_id', 'category_name')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        field = ('task_id', 'task_name')
