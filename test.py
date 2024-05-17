# test_todo_app.py

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from base.models import Todo

@pytest.mark.django_db
def test_todo_creation():
    todo = Todo.objects.create(title='Test Todo', description='This is a test todo item')
    assert todo.title == 'Test Todo'
    assert todo.description == 'This is a test todo item'
    assert not todo.completed

@pytest.mark.django_db
def test_todo_list_view(client):
    response = client.get(reverse('todo-list'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_todo_detail_view(client):
    todo = Todo.objects.create(title='Test Todo')
    response = client.get(reverse('todo-detail', kwargs={'pk': todo.pk}))
    assert response.status_code == 200