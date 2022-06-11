from rest_framework import serializers

from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['label', 'due_date', 'completed', 'completed_at', 'updated_at']