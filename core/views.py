from django.views.generic import ListView, DetailView
from .models import Post, Comment


class BlogIndexView(ListView):
    model = Post
    template_name = "blog_index.html"
    context_object_name = "posts"
    ordering = ["-created_on"]


class CategoryListView(ListView):
    model = Post
    template_name = "category.html"
    context_object_name = "posts"

    def get_queryset(self):
        category = self.kwargs["category"]
        return Post.objects.filter(categories__name__contains=category).order_by("-created_on")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        category = self.kwargs["category"]
        context["category"] = category
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["comments"] = Comment.objects.filter(post=self.object).order_by('-created_at')
        return context