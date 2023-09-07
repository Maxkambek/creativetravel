from django.contrib import admin
from .models import Hotel, AmenityGroup, DescriptionStruct, PolicyStruct, RoomGroups
from .models import Region

admin.site.register(Region)


class AmenAdmin(admin.StackedInline):
    model = AmenityGroup
    extra = 1


class DescriptionStructAdmin(admin.StackedInline):
    model = DescriptionStruct
    extra = 1


class PolicyStructAdmin(admin.StackedInline):
    model = PolicyStruct
    extra = 1


class RoomGroupsAdmin(admin.StackedInline):
    model = RoomGroups
    extra = 1


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    search_fields = ['sort_id']
    inlines = [AmenAdmin, DescriptionStructAdmin, RoomGroupsAdmin, PolicyStructAdmin]
