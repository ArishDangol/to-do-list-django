from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate

#routes always ends with forward slash => /
#URLConf
urlpatterns = [
     path('', TaskList.as_view(), name='tasks'),
     path('task/<int:pk>/', TaskDetail.as_view(), name ='task'),  # looks for pk ,pk = primary value
     path('task-create/', TaskCreate.as_view(), name='task-create'),
]



