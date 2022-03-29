from django.urls import path
from .views import TodoList, TodoUpdate, TodoCreate, TodoDelete, LoginView, Register
from .import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),

    path('', TodoList.as_view(), name='todos'),
    path('todo/<int:pk>/', TodoUpdate.as_view(), name='todo'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='delete'),

    path('yes_finish/<Todos_id>', views.yes_finish, name="yes_finish"),
    path('no_finish/<Todos_id>', views.no_finish, name="no_finish")
]