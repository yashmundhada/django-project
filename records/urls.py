from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "records"

urlpatterns = [
    path("onboarding/", views.onboarding, name="onboarding"),
    path("loandetails/", views.loanDetails, name="loandetails"),
    path("register/", views.register, name="register"),
] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
