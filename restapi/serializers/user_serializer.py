from rest_framework import serializers
from restapi.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_name', 'user_firstname', 'user_lastname',
        'email', 'password', 'create_at', 'last_login', 'board_records', 'user_delete')
