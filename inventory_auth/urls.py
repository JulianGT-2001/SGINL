from . import views
from django.urls import path

app_name = "inventory_auth"

urlpatterns = [
    path('', views.login_view, name='login')
]
