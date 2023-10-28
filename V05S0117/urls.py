from django.urls import path
from . import views

urlpatterns = [
    path('',views.current_datetime, name="home"),
    path('api/',views.api_response, name="api"),
    path('api/status',views.view_status, name="view_status"),
    path('api/newstatus/<str:pk>',views.change_status, name="change_status"),
]
