from django.db import models
from django.contrib.postgres.fields import ArrayField


class Hotel(models.Model):
    sort_id = models.CharField(max_length=2213, null=True)
    address = models.CharField(max_length=555, null=True, blank=True)
    check_in_time = models.CharField(max_length=1213, null=True, blank=True)
    check_out_time = models.CharField(max_length=1213, null=True, blank=True)
    kind = models.CharField(max_length=2213, null=True, blank=True)
    latitude = models.CharField(max_length=1001, null=True, blank=True)
    longitude = models.CharField(max_length=1001, null=True, blank=True)
    name = models.CharField(max_length=223, null=True, blank=True)
    phone = models.CharField(max_length=2222, null=True, blank=True)
    postal_code = models.CharField(max_length=1220, null=True, blank=True)
    star_rating = models.FloatField(default=0, null=True, blank=True)
    email = models.CharField(max_length=1231, null=True, blank=True)
    semantic_version = models.CharField(max_length=1000, null=True, blank=True)
    is_closed = models.BooleanField(default=False, null=True, blank=True)
    metapolicy_extra_info = models.TextField(null=True, blank=True)
    star_certificate = models.CharField(max_length=1234, null=True, blank=True)
    hotel_chain = models.CharField(max_length=2123, null=True, blank=True)
    front_desk_time_start = models.CharField(max_length=1213, null=True, blank=True)
    front_desk_time_end = models.CharField(max_length=1123, null=True, blank=True)
    is_gender_specification_required = models.BooleanField(default=False)
    images = ArrayField(models.CharField(max_length=1250), default=list)
    payment_methods = ArrayField(models.CharField(max_length=1250), default=list)
    country_code = models.CharField(max_length=4, null=True, blank=True)
    region_iata = models.CharField(max_length=5, null=True, blank=True)
    region_id = models.IntegerField(null=True, blank=True)
    region_name = models.CharField(max_length=1234, null=True, blank=True)
    region_type = models.CharField(max_length=1234, null=True, blank=True)
    serp_filters = ArrayField(models.CharField(max_length=1250), default=list)

    def __str__(self):
        return self.address


class AmenityGroup(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='amenity_group')
    group_name = models.CharField(max_length=2222, null=True, blank=True)
    amenities = ArrayField(models.CharField(max_length=1250), default=list)


class DescriptionStruct(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='description_struct')
    title = models.CharField(max_length=2222, null=True, blank=True)
    paragraphs = ArrayField(models.CharField(max_length=1250, null=True, blank=True), default=list)


class PolicyStruct(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, related_name='policy_struct')
    title = models.CharField(max_length=1000, null=True, blank=True)
    paragraphs = ArrayField(models.CharField(max_length=1250), default=list)


class RoomGroups(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, related_name='room_group')
    images = ArrayField(models.CharField(max_length=1250), default=list)
    name = models.CharField(max_length=1234, null=True, blank=True)
    room_amenities = ArrayField(models.CharField(max_length=2122, null=True, blank=True), default=list)
    room_group_id = models.IntegerField(null=True, blank=True)


class Region(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, db_index=True)
    iata = models.CharField(max_length=123, null=True, blank=True)
    country_name = models.CharField(max_length=2222, null=True, blank=True)
    country_code = models.CharField(max_length=223, null=True, blank=True)
    longitude = models.CharField(max_length=333, null=True, blank=True)
    latitude = models.CharField(max_length=333, null=True, blank=True)
    hotels = ArrayField(models.CharField(max_length=2122, null=True, blank=True), default=list)
    type = models.CharField(max_length=2222, null=True, blank=True)
    name = models.CharField(max_length=1234, null=True, blank=True)

    def __str__(self):
        return f'{self.id}'
