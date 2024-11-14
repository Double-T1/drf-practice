from . import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers, routers
"""
[<URLPattern '^snippets/$' [name='snippet-list']>, 
<URLPattern '^snippets\.(?P<format>[a-z0-9]+)/?$' [name='snippet-list']>, 
<URLPattern '^snippets/(?P<pk>[^/.]+)/$' [name='snippet-detail']>, 
<URLPattern '^snippets/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='snippet-detail']>, 
<URLPattern '^snippets/(?P<pk>[^/.]+)/highlight/$' [name='snippet-highlight']>, 
<URLPattern '^snippets/(?P<pk>[^/.]+)/highlight\.(?P<format>[a-z0-9]+)/?$' [name='snippet-highlight']>, 
<URLPattern '^users/$' [name='user-list']>, 
<URLPattern '^users\.(?P<format>[a-z0-9]+)/?$' [name='user-list']>, 
<URLPattern '^users/(?P<pk>[^/.]+)/$' [name='user-detail']>, 
<URLPattern '^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='user-detail']>, 
<URLPattern '' [name='api-root']>, 
<URLPattern '<drf_format_suffix:format>' [name='api-root']>]
"""
router = routers.DefaultRouter()
router.register(r"snippets", views.SnippetViewSet, basename='snippet')
router.register(r"users", views.UserViewSet, basename="user")
breakpoint()
urlpatterns = [
    path('', include(router.urls))
]

# snippet_list = views.SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# snippet_detail = views.SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# snippet_highlight = views.SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])

# user_list = views.UserViewSet.as_view({
#     'get': 'list'
# })

# user_detail = views.UserViewSet.as_view({
#     'get': 'retrieve'
# })


# urlpatterns = [
#     path('snippets/', snippet_list, name="snippet-list"), 
#     path('snippets/<int:pk>/', snippet_detail, name="snippet-detail"),
#     path('users/', user_list, name="user-list"),
#     path('users/<int:pk>/', user_detail, name="user-detail"),
#     path('', views.api_root),
#     path('snippets/<int:pk>/hightlight', snippet_highlight, name="snippet-highlight")
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

