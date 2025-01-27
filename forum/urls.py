from django.urls import include, path
from rest_framework import routers
from forum import views

router = routers.DefaultRouter()
router.register(r'answers', views.AnswerView)

urlpatterns = [
    path('', include(router.urls)),
]