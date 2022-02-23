
from django.urls import path,include
from . import views
from rest_framework import routers

router_generic= routers.DefaultRouter()
router_generic.register('articles', views.ArticleGenericViewSet, basename="generic")


router_viewset= routers.DefaultRouter()
router_viewset.register('articles', views.ArticleViewSet, basename="router_viewset")


router_model= routers.DefaultRouter()
router_model.register('articles', views.ArticleModelViewSet, basename="model")
router_model.register('users', views.UserModelViewSet, basename="users")


urlpatterns = [
    path('', views.index ),
    path('articles/',views.articles),
    path('api/articles/', views.articles_apiview),

    path('articles/<int:pk>/', views.articles_detail),
    path('api/articles/<int:pk>/', views.articles_detail_apiview),

    path('api/viewset/',include(router_viewset.urls)),

    path('api/generic/',include(router_generic.urls)),
    path('api/model/', include(router_model.urls)),
    # path('api/model/', include(router_model.urls))

]
