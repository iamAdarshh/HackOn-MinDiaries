from django.urls import path
from django.urls.resolvers import URLPattern

from .views import blogGrid, home, detailBlog

urlpatterns = [
    path('', view=home, name='home'),
    path('bloggrid/', view=blogGrid, name='bloggrid'),
    path('bloggrid/<blog_id>/', view=detailBlog, name='blog'),
]