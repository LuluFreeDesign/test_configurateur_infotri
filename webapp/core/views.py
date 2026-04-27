import os

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import TemplateView


def static_file_content_from(path):
    full_path = os.path.join(settings.BASE_DIR, "static", path)
    try:
        with open(full_path, "rb") as f:
            return HttpResponse(f.read(), content_type="application/javascript")
    except FileNotFoundError:
        return HttpResponse(
            f"// Script '{path}' not built yet — run: npm run build",
            content_type="application/javascript",
        )


class HomeView(TemplateView):
    template_name = "ui/pages/home.html"
