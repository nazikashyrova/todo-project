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

    def test_todo_detail_view(self):
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.get(reverse('todo', args=[self.todo1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Todo 1')

    def test_todo_creation_view(self):
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.post(reverse('create'), {'title': 'New Todo', 'complete': False})
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Todo.objects.filter(title='New Todo', user=self.user1).exists())

    def test_todo_update_view(self):
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.post(reverse('update', args=[self.todo1.id]), {'title': 'Updated Todo', 'complete': True})
        self.assertEqual(response.status_code, 302)
        self.todo1.refresh_from_db()
        self.assertEqual(self.todo1.title, 'Updated Todo')
        self.assertTrue(self.todo1.complete)

    def test_todo_delete_view(self):
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.post(reverse('delete', args=[self.todo1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(id=self.todo1.id).exists())

    def test_todo_permissions(self):
        self.client.login(username='testuser2', password='testpass2')
        response = self.client.get(reverse('todo', args=[self.todo1.id]))
        self.assertEqual(response.status_code, 403)  # Forbidden

    def test_todo_form_validation(self):
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.post(reverse('create'), {'title': '', 'complete': False})
        self.assertEqual(response.status_code, 200)  # Form re-rendered with errors
        self.assertFormError(response, 'form', 'title', 'This field is required.')

    def test_toggle_finish(self):
        self.client.login(username='testuser1', password='testpass1')
        # Toggle complete to True
        response = self.client.post(reverse('toggle_finish', args=[self.todo1.id]))
        self.assertEqual(response.status_code, 302)
        self.todo1.refresh_from_db()
        self.assertTrue(self.todo1.complete)
        # Toggle complete to False
        response = self.client.post(reverse('toggle_finish', args=[self.todo1.id]))
        self.assertEqual(response.status_code, 302)
        self.todo1.refresh_from_db()
        self.assertFalse(self.todo1.complete)

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser1', 'password': 'testpass1'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('todos'))

    def test_logout_view(self):
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))

    def test_register_view(self):
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'newpass123', 'password2': 'newpass123'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())
