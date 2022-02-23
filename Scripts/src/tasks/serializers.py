from rest_framework import serializers
from .models import Tasks, TASK_STATUS,Users




class TasksSerializer(serializers.Serializer):
    #
    # name = serializers.CharField(max_length=100)
    #
    # description = serializers.CharField(max_length=500)
    #
    # user_id = serializers.ForeignKey('Users')
    #
    # status = serializers.ChoiceField(choices=TASK_STATUS, default='Not-started')
    #
    # created_at = serializers.DateTimeField()
    #
    # updated_at = serializers.DateTimeField()
    #
    # def create(self, validated_data):
    #     """"
    #     Create and return a new `Tasks` instance, given the validated data.
    #
    #     """
    #     return Tasks.objects.create (validated_data)
    #
    # def update (self, instance, validated_data):
    #     """
    #    Update and return an existing task instance
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.status = validated_data.get('status', instance.status)
    #
    #     instance.save()
    #     return  instance


    # Model serializers
    class Meta:
        model = Tasks
        fields = ['name', 'description','user_id']

class UsersSerializer(serializers.Serializer):
    class Meta:
        model: Users
        fields : '__all__'

