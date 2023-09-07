from django.urls import path
from .views import HotelListAPIView, RegionListAPIView, GetHotelPageAPIView

urlpatterns = [
    path('hotel/', HotelListAPIView.as_view()),
    path('region/', RegionListAPIView.as_view()),
    path('get-hotelpage/', GetHotelPageAPIView.as_view())
]
