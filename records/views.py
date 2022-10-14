from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
def onboarding(request):
    return render(request, "onboarding.html")


def loanDetails(request):
    return render(request, "loanDetails.html")


def checkbase(request):
    return render(request, "checkingBase.html")


def base(request):
    return render(request, "base.html")


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")

        if request.FILES:
            files = request.FILES["file"]
            fs = FileSystemStorage()
            savedfiles = fs.save(files.name, files)
            file_url = fs.url(savedfiles)

        return HttpResponse(
            "<h1> {} {} {} {} , <img src={}></h1>".format(
                name, age, gender, files, file_url
            )
        )

    return render(request, "register.html")
