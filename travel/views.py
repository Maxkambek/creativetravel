from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import json
from .models import Hotel, Region
from .serializers import HotelSerializers, RegionSerializer


def getPrice(ids):
    url = "https://api.worldota.net/api/b2b/v3/search/serp/hotels/"
    payload = json.dumps({
        "checkin": "2023-08-25",
        "checkout": "2023-08-26",
        "residency": "uz",
        "language": "en",
        "guests": [
            {
                "adults": 2,
                "children": []
            }
        ],
        "ids": list(ids)[:10],
        "currency": "EUR"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic NDkzMDo0M2EzM2EyYS1jYTYwLTRkMzItOTM5NC0wM2U3ZWQ0MTM1NzI=',
        'Cookie': 'uid=TfTb8GSEOdcwJ1YlA2LCAg=='
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


class GetHotelPageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        sort_id = self.request.GET.get('sort_id')
        region = Region.objects.filter(id=sort_id).first()
        res = getPrice(region.hotels)
        # print(res)
        data = []
        if not res:
            return Response('error')
        for i in res['data']['hotels']:
            print(i['id'])
            hotel = Hotel.objects.filter(sort_id=i['id']).first()

            if hotel:
                data.append(dict(
                    id=i['id'],
                    rates=i['rates'],
                    name=hotel.name,
                    images=hotel.images
                ))
        return Response(data)


class RegionListAPIView(generics.ListAPIView):
    serializer_class = RegionSerializer

    def get_queryset(self):
        queryset = Region.objects.all()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(iata__icontains=search)
        if len(queryset) < 1:
            queryset = queryset.filter(country_name__icontains=search)
        if len(queryset) < 1:
            queryset = queryset.filter(name__icontains=search)
        return queryset


class HotelListAPIView(generics.ListAPIView):
    serializer_class = HotelSerializers

    def get_queryset(self):
        queryset = Hotel.objects.all()
        sort_id = self.request.GET.get('sort_id')
        region_id = self.request.GET.get('region_id')
        if region_id:
            queryset = queryset.filter(region_id=region_id)
        if sort_id:
            queryset = queryset.filter(sort_id=sort_id)
        return queryset
