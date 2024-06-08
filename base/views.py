from datetime import datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.utils import translation

from django.shortcuts import render
from django.http import HttpResponse, Http404

from django.contrib.auth.views import redirect_to_login
from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Todo

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

class LogoutView(BaseLogoutView):
    next_page = reverse_lazy('login')

class LoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todos')


class Register(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todos')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('todos')
        return super(Register, self).get(*args,**kwargs)


class TodoList(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'todos'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = context['todos'].filter(user=self.request.user)
        context['count'] = context['todos'].filter(complete=False).count

        search = self.request.GET.get('search') or ''
        search = search[1:]
        if search:
            context['todos'] = context['todos'].filter(title__icontains=search)

        filter = self.request.GET.get('filter') or ''
        if filter:
            if filter == 'finished':
                context['todos'] = context['todos'].filter(complete=True)
            if filter == 'notfinished':
                context['todos'] = context['todos'].filter(complete=False)
            if filter == 'today':
                context['todos'] = context['todos'].filter(created__range=[datetime.now() - timedelta(days=1), datetime.now()])
            if filter == 'last3':
                context['todos'] = context['todos'].filter(created__gte=datetime.now() - timedelta(days=3))
            if filter == 'lastweek':
                context['todos'] = context['todos'].filter(created__gte=datetime.now() - timedelta(days=7))
            if filter == 'last30':
                context['todos'] = context['todos'].filter(created__gte=datetime.now() - timedelta(days=30))
            if filter == 'lastyear':
                context['todos'] = context['todos'].filter(created__gte=datetime.now() - timedelta(days=365))
        sort = self.request.GET.get('sort') or ''
        if sort:
            context['todos'] = context['todos'].order_by(sort)

        if sort == '-complete':
            context['angle1'] = '1'
        else:
            context['angle1'] = '0'

        if sort == '-title':
            context['angle2'] = '1'
        else:
            context['angle2'] = '0'

        if sort == '-created':
            context['angle3'] = '1'
        else:
            context['angle3'] = '0'

        context['search1'] = search
        return context

 
class TodoCreate(CreateView):
    model = Todo
    fields = ['title','description','complete']
    success_url = reverse_lazy('todos')
    template_name = 'base/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreate, self).form_valid(form)


class TodoUpdate(UpdateView):
    model = Todo
    fields = ['title','description']
    template_name = 'base/update.html'
    success_url = '/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TodoUpdate, self).dispatch(*args, **kwargs)

    def get_object(self, *args, **kwargs):
        obj = super(TodoUpdate, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise Http404
        return obj

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoUpdate, self).form_valid(form)


class TodoDelete(LoginRequiredMixin,DeleteView):
    model = Todo
    context_object_name = 'todo'
    success_url = reverse_lazy('todos')
    template_name = 'base/confirm_delete.html'


def toggle_finish(request, Todos_id):
    todo = get_object_or_404(Todo, pk=Todos_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("todos")