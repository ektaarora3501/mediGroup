from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'posts_detail.html'

class PostCreate(LoginRequiredMixin, CreateView):
    template_name = 'posts_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(PostCreate, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(PostCreate, self).get_context_data(*args, **kwargs)
        return context
