from django.shortcuts import render, redirect
from .models import Person
from django.contrib import messages
from .forms import CreatePerson, UpdatePerson


# Create your views here.
def homepage(request):
    all = Person.objects.all()
    return render(request, "home.html", context={"people": all})


def details(request, person_id):
    _id = Person.objects.get(id=person_id)
    return render(request, "details.html", {"id": _id})


def delete(request, person_id):
    Person.objects.get(id=person_id).delete()
    messages.success(
        request, "Person deleted successfully", extra_tags="alert alert-success"
    )
    return redirect("home")


def create_user(request):
    if request.method == "POST":
        form = CreatePerson(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Person.objects.create(
                name=cd["first_name"] + " " + cd["last_name"],
                age=cd["age"],
            )
            messages.success(
                request, "Person created successfully", extra_tags="alert alert-success"
            )
            return redirect("home")
    else:
        form = CreatePerson()
    return render(request, "create.html", {"form": form})


def update_user(request, person_id):
    person = Person.objects.get(id=person_id)
    if request.method == "POST":
        form = UpdatePerson(request.POST, instance=person)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Person updated successfully", extra_tags="alert alert-success"
            )
            return redirect("details", person_id)
    else:
        form = UpdatePerson(instance=person)
    return render(request, "update.html", {"form": form})
