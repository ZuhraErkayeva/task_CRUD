from django.urls import path
from crud_project.views import TaskListView, TaskUpdateView, TaskCreateView, TaskDeleteView, LoginView, RegisterView,logout_view

urlpatterns = [
    path('task/', TaskListView.as_view(), name='task-list'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('', RegisterView.as_view(), name='register'),
    path('logout/',logout_view,name = 'logout')
]


