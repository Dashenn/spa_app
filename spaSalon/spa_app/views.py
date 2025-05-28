from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Specialist, Review, Service, ServiceCategory, Request
from .forms import RequestForm


def index(request):
    categories = ServiceCategory.objects.all()
    specialists = Specialist.objects.all()
    reviews = Review.objects.all()
    services = Service.objects.all()

    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            service = (
                Service.objects.get(id=data["desired_service"])
                if data["desired_service"]
                else None
            )
            Request.objects.create(
                first_name=data["first_name"],
                last_name=data["last_name"],
                phone_number=data["phone_number"],
                desired_service=service,
            )
            messages.success(request, "Ваша заявка успешно отправлена!")
            return redirect("index")
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = RequestForm()

    return render(
        request,
        "spa_app/main.html",
        {
            "categories": categories,
            "specialists": specialists,
            "reviews": reviews,
            "services": services,
            "form": form,
        },
    )


def about(request):
    return render(request, "spa_app/about.html")


def services(request):
    return render(request, "spa_app/services.html")


def contact(request):
    return render(request, "spa_app/contact.html")
