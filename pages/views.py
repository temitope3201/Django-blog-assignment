from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CommentForm

# Create your views here.

class BlogPostViews(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailedView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    form_class = CommentForm()

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user 



