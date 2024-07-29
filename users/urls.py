from django.urls import path
from . import views
from .views import UserProfileView, PaymentListView

app_name = 'users'

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('payments/', PaymentListView.as_view(), name='payment-list'),
]
