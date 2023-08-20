from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render

from .forms import CommentForm
from .models import Post, Comment


class HomeView(ListView):
    model = Post
    template_name = 'atomy/home.html'


class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


def home(request):
    return render(request, 'base.html')

class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()
