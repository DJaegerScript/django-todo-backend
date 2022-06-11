import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todo.models import Todo

from todo.serializers import TodoSerializer
# Create your views here.
class TodoApiView(APIView):
    def post(self, request):
        data = {
            'label' : request.data.get('label'),
            'due_date' : request.data.get('dueDate'),
        }
        
        serializer = TodoSerializer(data = data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class TodoDetailApiView(APIView):
    def get_data(self, todo_id):
        try:
            return Todo.objects.get(id=todo_id)
        except:
            return None
        
    def get(self, _, todo_id):
        todo_instance = self.get_data(todo_id)
        
        if not todo_instance:
            return Response({"message" : 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)
        
        todo = TodoSerializer(todo_instance)
        return Response(todo.data, status=status.HTTP_200_OK)
    
    def put(self, request, todo_id):
        todo_instance = self.get_data(todo_id)
        
        if not todo_instance:
            return Response({"message" : 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)
        
        data = {
            "label": request.data.get("label") or todo_instance.label,
            "due_date": request.data.get("dueDate") or todo_instance.due_date,
            "completed": request.data.get("completed") or todo_instance.completed,
            "completed_at": datetime.datetime.now() if request.data.get("completed") else None,
        }
        
        
        todo = TodoSerializer(instance=todo_instance, data=data, partial=True)
        
        if not todo.is_valid():
            return Response(todo.errors, status=status.HTTP_400_BAD_REQUEST)
        

        todo.save()
        return Response(todo.data, status=status.HTTP_200_OK)
    
    def delete(self, _, todo_id):
        todo_instance = self.get_data(todo_id)
        
        if not todo_instance:
            return Response({"message" : 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)
        
        todo_instance.delete()
        return Response({"message": "Data successfully deleted"}, status=status.HTTP_200_OK)

        

        
        