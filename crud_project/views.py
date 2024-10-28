from django.contrib.auth.decorators import login_required
from django.template.context_processors import request
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from crud_project.forms import CustomUserCreationForm, LoginForm
from crud_project.models import Task
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'dashboard.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)



class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'create-task.html'
    fields = ['title', 'status', 'due_date']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task-list')


class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'edit-task.html'
    fields = ['title','status','due_date']

    def get_success_url(self):
        return reverse_lazy('task-list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'dashboard.html'

    def get_success_url(self):
        return reverse_lazy('task-list')


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Email yoki parol noto'g'ri.")
            return self.form_invalid(form)



class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        return response

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')