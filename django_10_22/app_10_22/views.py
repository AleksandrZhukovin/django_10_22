from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import TaskCreateForm, RegistrationForm, LoginForm, ProjectForm, TestForm
from django.contrib.auth import login, authenticate
from .models import Project, Task
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User(username=name, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'home.html', context)


class Registration(CreateView):
    template_name = 'registration.html'
    model = User
    # fields = ['username', 'email', 'password1', 'password2']
    form_class = RegistrationForm
    success_url = reverse_lazy('home')


class LoginPage(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_authenticated_user = True


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/login')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'home.html', context)


def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'home.html', context)


class Home(ListView):
    template_name = 'home.html'
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            project = Project(name=name)
            project.save()
            return redirect('/')
    else:
        form = ProjectForm()
        return render(request, 'project_create.html', {'form', form})


def project(request, **kwargs):
    project = Project.objects.get(id=kwargs['id'])
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            status = form.cleaned_data['status']
            deadline = form.cleaned_data['deadline']
            number = form.cleaned_data['number']
            task = Task(text=text, number=number, status=status, deadline=deadline, project=project)
            task.save()
            return redirect('/')
    else:
        tasks = Task.objects.filter(project=project)
        form = TaskCreateForm()
        context = {'form': form, 'tasks': tasks, 'project': project}
        return render(request, 'project.html', context)


def edit_project(request, **kwargs):
    project = Project.objects.get(id=kwargs['id'])
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            project.name = name
            project.save()
            return redirect('/')
    else:
        form = ProjectForm()
        return render(request, 'project_create.html', {'form', form})


class ProjectEditPage(UpdateView):
    model = Project
    template_name = 'project_edit.html'
    form_class = ProjectForm
    success_url = reverse_lazy('/')


class FormPage(FormView):
    template_name = 'form.html'
    form_class = TestForm
    success_url = reverse_lazy('/')

    def form_valid(self, form):
        response = HttpResponse()
        response.set_cookie('name', form.cleaned_data['name'])
        return super().form_valid(form)


class TestPage(TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_dat(**kwargs)
        context['title'] = 'Test Page'
        return context

    def post(self, request):
        data = request.POST
        print(data['test'])