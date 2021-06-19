from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView
    
)
from . import views

urlpatterns = [
    path('', PostListView.as_view() , name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view() , name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view() , name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view() , name='post-delete'),
    path('post/new/', PostCreateView.as_view() , name='post-create'),
    path('about/', views.about, name='blog-about'),
]

# . is current directory
# An /instance of HttpRequest/.
# If the matched URL pattern contained no named groups, then the matches from the /regular expression are provided as positional arguments/.
# The keyword arguments are made up of /any named parts matched by the path expression/ that are provided, overridden by any arguments specified in the optional kwargs argument to django.urls.path() or django.urls.re_path().    

# <app>/<model>_<viewtype>.html