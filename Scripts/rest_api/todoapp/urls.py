
from django.urls import path,include
from . import views
from rest_framework import routers

router_model= routers.DefaultRouter()
router_model.register('todos', views.TodoModelViewSet, basename="todos")

router_users = routers.DefaultRouter()
router_users.register('', views.UserViewSet, basename="users")


urlpatterns = [

    path('todo/', views.TodoList.as_view()),
    path('todo/<int:pk>', views.TodoDetail.as_view()),
    path('users/', include(router_users.urls)),
    path('auth/', views.ObtainAuthTokenForUser.as_view()),

]
