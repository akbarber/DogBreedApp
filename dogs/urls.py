from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from dogs import views   
from django.views.decorators.csrf import csrf_exempt


router = routers.DefaultRouter(trailing_slash=False)


urlpatterns = [   
    url(r'^dogs', csrf_exempt(views.DogList.as_view()), name='dog-list'),
    url(r'^dogs/<int:pk>', csrf_exempt(views.DogDetail.as_view()), name='dog-detail'),
    url(r'^breeds', csrf_exempt(views.BreedList.as_view()), name='breed-list'),
    url(r'^breeds/<int:pk>', csrf_exempt(views.BreedDetail.as_view()), name='breed-list'),
    url(r'^', include(router.urls)),
    path('', views.api_root, name='api-root'),
]

#urlpatterns = format_suffix_patterns(urlpatterns)