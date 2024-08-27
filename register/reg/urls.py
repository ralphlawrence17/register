from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.stud_list, name='students'),
    path('create/', views.stud_create, name='stud_create'),
    path('update/<int:pk>/', views.stud_update, name='stud_update'),
    path('delete/<int:pk>/', views.stud_delete, name='stud_delete'),

    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),

    path('subjects/', views.sub_list, name='subjects'),
    path('subjects/create', views.sub_create, name='sub_create'),
    path('subjects/update/<int:pk>', views.sub_update, name='sub_update'),
    path('subjects/delete/<int:pk>/', views.sub_delete, name='sub_delete'),

    path('teachers/', views.teacher_list, name='teachers'),
    path('teachers/create/', views.teacher_create, name='teacher_create'),
    path('teachers/update/<int:pk>', views.teacher_update, name='teacher_update'),
    path('teachers/delete/<int:pk>/', views.teacher_delete, name='teacher_delete'),

    path('position/', views.position_list, name='positions'),
    path('position/create/', views.add_position, name='add_position'),
    path('position/update/<int:pk>', views.update_position, name='update_position'),
    path('position/delete/<int:pk>/', views.delete_position, name='delete_position'),
]
