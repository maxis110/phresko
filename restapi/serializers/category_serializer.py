from rest_framework import serializers
from restapi.models.category import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = ('category_id', 'category_name')
