from django.urls import path

from todo.views import TodoApiView, TodoDetailApiView


urlpatterns = [
    path('', TodoApiView.as_view()),
    path('<int:todo_id>', TodoDetailApiView.as_view())
]
