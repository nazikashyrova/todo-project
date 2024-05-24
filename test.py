from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from base.models import Todo

class TodoTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='testpass1')
        self.user2 = User.objects.create_user(username='testuser2', password='testpass2')
        
        self.todo1 = Todo.objects.create(title='Test Todo 1', complete=False, user=self.user1)
        self.todo2 = Todo.objects.create(title='Test Todo 2', complete=False, user=self.user2)

    def test_todo_creation(self):
        self.assertEqual(self.todo1.title, 'Test Todo 1')
        self.assertFalse(self.todo1.complete)
        self.assertEqual(self.todo1.user, self.user1)

    def test_todo_update(self):
        self.todo1.complete = True
        self.todo1.save()
        updated_todo = Todo.objects.get(pk=self.todo1.pk)
        self.assertTrue(updated_todo.complete)

    def test_todo_delete(self):
        todo_count = Todo.objects.count()
        self.todo1.delete()
        self.assertEqual(Todo.objects.count(), todo_count - 1)

    def test_todo_list_view(self):
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.get(reverse('todos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Todo 1')
        self.assertNotContains(response, 'Test Todo 2')
