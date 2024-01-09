from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import contactviewset


router = routers.DefaultRouter()
router.register(r'contact', views.contactviewset, basename='contact')
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('', include(router.urls), name="contact"),
    path('about_us/', views.about_us, name='about_us'),
    path('policy/', views.policy, name='policy'),
    path('search/', views.search.as_view(), name='search'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
