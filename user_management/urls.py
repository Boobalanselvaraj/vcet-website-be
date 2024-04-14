from django.urls import path
from .views import save_email

urlpatterns = [
    path('user/save-email/', save_email, name='save_email'),
]