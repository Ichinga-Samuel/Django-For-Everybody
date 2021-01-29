from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('test', views.dje),
    path('<int:post_id>/share', views.share_post, name='share_post'),
    path('tag/<slug:tag_slug>', views.post_list, name='post_list_tag')

]
