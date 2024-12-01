from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.BlogIndexView.as_view(), name="blog_index"),
    path("categories/<category>", views.CategoryListView.as_view(), name="categories"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)