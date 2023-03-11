from django.contrib import admin
from django.urls import path
from . import views

app_name = "base"
urlpatterns = [
    path("", views.index, name='index'),
    path("book", views.book, name="book"),
    # path("pay/<int:pk>", views.pay, name="pay"),
    # path("payment", views.handle_pay, name="handle_pay"),

]


admin.site.site_header = 'Royal Palace Hotel'                    # default: "Django Administration"
admin.site.index_title = 'Admin panel'                 # default: "Site administration"
admin.site.site_title = 'Royal Palace Hotel' # default: "Django site admin"