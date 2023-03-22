from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import F
from .models import Customer, Room
from .form import PayForm


# Create your views here.


def index(request):
    return render(request, "base/index.html")


def book(request):
    # rooms = Room.objects.select_related('category')
    rooms = Room.objects.raw("SELECT * FROM base_room INNER JOIN base_category ON base_room.category_id = "
                             "base_category.id WHERE base_room.id NOT IN (SELECT room_id_id FROM base_customer WHERE "
                             "active = 1)")

    print(rooms)
    return render(request, "base/book.html", {"rooms": list(rooms)})


def pay(request, pk):
    
    submitted = False
    
    form = PayForm()
    room = Room.objects.select_related("category")
    context = {"form": form, "room": room, "id": pk}
    return render(request, "base/pay.html", context)


def handle_pay(request):
    if request.POST:
        try:
            form = PayForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("base:book", current_app="base"))

            # first_name = request.POST["first_name"]
            # last_name = request.POST["last_name"]
            # email = request.POST["email"]
            # city = request.POST['city']
            # phone_number = request.POST['phone_number']
            # id_number = request.POST['id_number']
            # room_id = int(request.POST['room_id'])
            # customer = Customer.objects.create(
            #     first_name=first_name,
            #     last_name=last_name,
            #     email=email,
            #     city=city,
            #     phone_number=phone_number,
            #     id_number=id_number,
            #     room_id=room_id
            # )
            # customer.save()
        except Exception as e:
            error_message = e
            context = {'error_message': error_message}
            return HttpResponse(e)
            # return HttpResponseRedirect(reverse("base:pay", current_app="base", args=(room_id,)), context)
    else:
        return HttpResponseRedirect(reverse("book", current_app="base"))
