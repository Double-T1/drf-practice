from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers

snippet_list = views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = views.UserViewSet.as_view({
    'get': 'list'
})

user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    path('snippets/', snippet_list, name="snippet-list"), 
    path('snippets/<int:pk>/', snippet_detail, name="snippet-detail"),
    path('users/', user_list, name="user-list"),
    path('users/<int:pk>/', user_detail, name="user-detail"),
    path('', views.api_root),
    path('snippets/<int:pk>/hightlight', snippet_highlight, name="snippet-highlight")
]

urlpatterns = format_suffix_patterns(urlpatterns)

