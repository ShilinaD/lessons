from django.urls import path

from main.views import WomenAPIView

urlpatterns = [
    path('api/v1/womenlist/', WomenAPIView.as_view())
]