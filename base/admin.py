from django.contrib import admin
from .models import Category, Customer, Room

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name",
                    "email", "phone_number", 'active', 'room_id']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","categories", 'beds', 'price']


class RoomAdmin(admin.ModelAdmin):
    list_display = ["id", 'category',  'room_code']

admin.site.site_header = "Royal Palace Hotel"
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Room, RoomAdmin)
