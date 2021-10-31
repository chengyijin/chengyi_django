from django.urls import path

from . import views, testdb, search, post

urlpatterns = [
    path(route='runoob', view=views.runoob, kwargs=None, name=None),
    path(route='testdb/', view=testdb.delete, kwargs=None, name=None),
    path(route='search-form/', view=search.search_form, kwargs=None, name=None),
    path(route='search/', view=search.search, kwargs=None, name=None),
    path(route='search-post/', view=post.search_post, kwargs=None, name=None),
]
