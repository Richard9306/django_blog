from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView

from .forms import CommentForm
from .models import Post, Comment


class BlogIndexView(ListView):
    model = Post
    template_name = "core/blog_index.html"
    context_object_name = "posts"
    ordering = ["-created_on"]


class CategoryListView(ListView):
    model = Post
    template_name = "core/category.html"
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
    template_name = "core/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["comments"] = Comment.objects.filter(post=post).order_by('-created_on')
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(requet.POST)

        if form.is_valid():
            Comment.objects.create(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            return HttpResponseRedirect(self.request.path_info)
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)
