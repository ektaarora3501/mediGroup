from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostsCreateForm, PostsAboutCreateForm
from group.models import Register

class PostList(ListView):
    template_name = 'dashboard.html'
    def get_queryset(self):
        return Posts.objects.all()

class PostDetail(DetailView):
    template_name = 'post_detail.html'
    def get_queryset(self):
        return Posts.objects.all()

class PostCreate(CreateView):
    form_class = PostsAboutCreateForm
    template_name = 'post_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(PostCreate, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(PostCreate, self).get_context_data(*args, **kwargs)
        return context
