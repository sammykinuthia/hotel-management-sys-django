from django.urls import path
from . import views

app_name = "base"
urlpatterns = [
    path("", views.index, name='index'),
    path("book", views.book, name="book"),
    path("pay/<int:pk>", views.pay, name="pay"),
    path("payment", views.handle_pay, name="handle_pay"),

]
