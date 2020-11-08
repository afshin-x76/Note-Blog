from django.urls import path
from .views import index, post, blog


urlpatterns = [
    path('', index),
    path('blog/', blog),
    path('posts/<int:id>/', post, name='post'),
]