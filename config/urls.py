from django.urls import include, path
from rest_framework import routers
from snippets import views


router = routers.DefaultRouter()

urlpatterns = [
    # path('', include(router.urls)),
    path('', include('snippets.urls')),
]

urlpatterns += [path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))]


