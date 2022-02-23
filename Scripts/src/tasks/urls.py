from django.urls import path
from . import views
from django.http import HttpResponse


urlpatterns = [
    path('',views.index, name='home'),
    path('signup/',views.signup,name='signup'),
    path('signup/<int:id>', views.signup, name='edit-user'),
    path('tasks/create/',views.createOrUpdate, name='create'),
    path('tasks/update/<int:id>',views.createOrUpdate, name='update'),
    path('tasks/delete/<int:id>',views.delete, name='delete'),

]
