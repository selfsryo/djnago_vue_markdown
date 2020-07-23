from django.urls import include, path
from . import views 

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/posts/', views.PostList.as_view(), name='post'),
]
