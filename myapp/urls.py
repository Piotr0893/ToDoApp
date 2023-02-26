from django.urls import path
from . import views 

urlpatterns = [
  path('', views.Task_List, name = 'Task_List'),
  path('task_show/<task_id>', views.Task_Show, name ='Task_Show'),
  path('add_task', views.Add_Task, name='Add_Task'),
  path('update_task/<task_id>', views.Update_Task, name ='Update_Task'),
  path('delete_task/<task_id>', views.Delete_Task, name ='Delete_Task'),
  path('search_task', views.Search_Task, name="Search_Task"),
  path('not_complete/<task_id>',views.Not_Complete, name='Not_Complete'),
  path('complete/<task_id>',views.Complete, name='Complete'),
    
]