from django.conf import settings
from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token




class MyUserSerializer(serializers.Serializer):

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = '__all__'


class ArticleSerializer(serializers.Serializer):
    created = serializers.DateTimeField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()

    def create(self, validated_data):
        return Article.objects.creata(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)


class ArticleModelSerializer(serializers.ModelSerializer):
    # articles = serializers.PrimaryKeyRelatedField(many=True,queryset=Article.objects.all())
    class Meta:
        model = Article
        fields = '__all__'

# for registration
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','password']

        extra_kwargs = {
            'password' : {
                'write_only':True,
                'required':True
            }
        }

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

