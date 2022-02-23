from django.conf import settings
from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Todo
        fields = '__all__'


class UserSerializerWithTodo(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Todo.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'todos', 'password']

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            },

        }

    #
    def create(self, validated_data):
        username = validated_data.pop('username')
        print('username', username)
        user = User(username=username)
        user.set_password(validated_data['password'])
        user.save()
        user.todos.set([])
        user.save()
        # Token.objects.create(user=user)
        return user
