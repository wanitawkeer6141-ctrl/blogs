from django.urls import path
from. import views


urlpatterns = [
    path('',views.home_page,name = 'home'),
    path("allposts/",views.blogsposts,name = 'allposts'),
    path("allposts/<slug:blog>/",views.blog_post,name = 'blog-post') # add key value name init 
    
]


