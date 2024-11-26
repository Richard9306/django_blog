from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.BlogIndexView.as_view(), name="blog_index"),
    path("categories/<category>", views.CategoryListView.as_view(), name="categories"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail")
]
