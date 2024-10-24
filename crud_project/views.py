from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from crud_project.models import Task
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


class TaskListView(ListView):
    model = Task
    template_name = 'dashboard.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'create-task.html'
    fields = ['title', 'status', 'due_date']

    def get_success_url(self):
        return reverse_lazy('task-list')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'edit-task.html'
    fields = ['title','status','due_date']

    def get_success_url(self):
        return reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'dashboard.html'

    def get_success_url(self):
        return reverse_lazy('task-list')



class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        return response


def logout_view(request):
    logout(request)
    return redirect('login')