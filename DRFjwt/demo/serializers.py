
from rest_framework import serializers
from demo.models import User, Task


class UserSerializer(serializers.ModelSerializer):
    
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
    
    class Meta:
        model = User
        fields = ('email', 'last_login', 'is_admin', 'tasks', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    


class TaskSerializer(serializers.ModelSerializer):
    
    person = serializers.SlugRelatedField(slug_field = User.USERNAME_FIELD, queryset = User.objects.all())
    
    class Meta:
        model = Task
        fields = ('title', 'person', 'due_to')

