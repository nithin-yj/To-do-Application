from django.urls import path
from .views import register,login_view,home,logout_view,todo_list,add_task,edit_task,delete_task

urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('',home,name='home'),
    path('list/',todo_list,name='list'),
    path('addtask/',add_task,name='add'),
    path('edittask/<int:pk>/',edit_task,name='edit'),
    path('deletetask/<int:pk>/',delete_task,name='delete'),
]
