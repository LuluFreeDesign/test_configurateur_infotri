from django.urls import include, path

from core.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("infotri/", include("infotri.urls")),
    path("infotri-asl/", include("infotri_asl.urls")),
]
