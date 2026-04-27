from django.urls import path

from . import views

app_name = "infotri_asl"

urlpatterns = [
    path("", views.InfotriAslConfiguratorView.as_view(), name="configurator"),
    path("embed", views.InfotriAslEmbedView.as_view(), name="embed"),
    path("iframe.js", views.get_infotri_asl_iframe_script, name="iframe_script"),
    path("configurateur.js", views.get_infotri_asl_configurator_iframe_script, name="configurator_script"),
]
