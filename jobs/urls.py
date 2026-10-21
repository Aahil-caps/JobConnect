from django.urls import path
from .import views


urlpatterns = [
    path('jobs/',views.job_list,name='job_list'),
    path('jobs/<int:pk>/',views.job_detail,name='job_detail'),
    path('jobs/create/',views.job_create,name='job_create'),
    path('jobsdel/<int:pk>/',views.job_delete,name='job_delete'),
    path('jobsup/<int:pk>/',views.job_update,name='job_update'),
    path('register/',views.register_user,name='register'),
    path('login/',views.login_user,name='login_user'),
    path('logout/',views.logout_user,name='logout_user'),
]