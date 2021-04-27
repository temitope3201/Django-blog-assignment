from django.urls import path
from .views import BlogPostViews, BlogDetailedView, BlogCreateView, BlogUpdateView,BlogDeleteView


urlpatterns = [
    path('', BlogPostViews.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailedView.as_view(), name='post_detail'),
    path('post/new', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]