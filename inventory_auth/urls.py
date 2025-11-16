from . import views
from django.urls import path

app_name = "inventory_auth"

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
