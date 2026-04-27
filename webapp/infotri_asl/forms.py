from django import forms
from dsfr.forms import DsfrBaseForm

from .constants import TYPE_PRODUIT_CHOICES, VERSION_CHOICES


class InfotriAslForm(DsfrBaseForm):
    """Formulaire QCM du configurateur Info-tri ASL."""

    # Étape 1 : type de produit → détermine les destinations automatiquement
    type_produit = forms.ChoiceField(
        choices=TYPE_PRODUIT_CHOICES,
        label="",
        required=False,
        widget=forms.RadioSelect(),
    )

    # Étape 2 : nom du produit en texte libre → affiché dans le SVG
    nom_produit = forms.CharField(
        label="Nom du produit concerné",
        max_length=40,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "ex : vélo, raquette, casque...",
            "class": "fr-input",
            "autocomplete": "off",
        }),
    )

    # Étape 3 : version de l'info-tri
    version = forms.ChoiceField(
        choices=VERSION_CHOICES,
        label="",
        required=False,
        initial="redigee",
        widget=forms.RadioSelect(),
    )
