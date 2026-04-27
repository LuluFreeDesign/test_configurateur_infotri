from typing import Any

from django.conf import settings
from django.views.generic import FormView

from core.views import static_file_content_from
from infotri_asl.constants import (
    AVEC_CONSEIL_REPARATION_BY_TYPE,
    DEST_COMBO_SVG_TEMPLATES,
    TEXTE_PRODUIT_BY_TYPE,
)
from infotri_asl.forms import InfotriAslForm


def get_infotri_asl_iframe_script(request):
    return static_file_content_from("embed/infotri-asl.js")


def get_infotri_asl_configurator_iframe_script(request):
    return static_file_content_from("embed/infotri-asl-configurator.js")


class InfotriAslConfiguratorView(FormView):
    """
    Configurateur Info-tri pour la filière ASL (Articles de Sports et Loisirs) — ECOLOGIC.

    QCM en 3 étapes :
      1. Choix du type de produit → détermine la combinaison de destinations
      2. Saisie du nom du produit (texte libre → rendu dynamiquement dans le label)
      3. Choix de la version (rédigée / semi-rédigée)
    """

    form_class = InfotriAslForm
    template_name = "ui/pages/infotri_asl.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.GET:
            kwargs["data"] = self.request.GET
        return kwargs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["base_url"] = settings.BASE_URL
        context["show_code"] = self.request.GET.get("show_code") == "true"

        type_produit = self.request.GET.get("type_produit", "")
        version = self.request.GET.get("version", "redigee")

        # SVG du label complet (destinations incluses) selon le type
        context["dest_combo_svg_template"] = DEST_COMBO_SVG_TEMPLATES.get(type_produit)

        # Texte d'en-tête du cartouche produit
        context["texte_produit"] = TEXTE_PRODUIT_BY_TYPE.get(type_produit, "CET ARTICLE SE TRIE")

        # Affichage du conseil réparation/don
        context["avec_conseil_reparation"] = AVEC_CONSEIL_REPARATION_BY_TYPE.get(
            type_produit, True
        )

        # La version rédigée montre le texte d'en-tête
        context["version"] = version

        return context

    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class InfotriAslEmbedView(InfotriAslConfiguratorView):
    """Vue embed — chargée en iframe sur les sites tiers."""

    template_name = "ui/pages/infotri_asl_embed.html"
