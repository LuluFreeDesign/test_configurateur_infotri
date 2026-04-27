"""Constants for Info-tri ASL (Articles de Sports et Loisirs) — filière ECOLOGIC."""

# ---------------------------------------------------------------------------
# QCM — Étape 1 : Choix du type de destination
# Chaque choix correspond à une des 4 combinaisons de destinations réglementaires
# La combinaison choisie détermine : le SVG affiché, le texte produit, et les infos additionelles
# ---------------------------------------------------------------------------
TYPE_PRODUIT_CHOICES = [
    (
        "asl_general",
        "Article de sport ou loisir — Association OU Magasin OU Déchèterie"
        " (ex : vélo, raquette, surf, paddle, ballon, trampoline...)",
    ),
    (
        "gros_asl",
        "Gros article de sport — Association OU Reprise à domicile OU Déchèterie"
        " (ex : table de ping-pong, table de billard...)",
    ),
    (
        "epi",
        "Équipement de protection individuelle — Magasin OU Déchèterie"
        " (ex : casque, genouillères, masque de ski, gilet de sauvetage...)",
    ),
    (
        "chasse_tir",
        "Équipement de chasse et tir sportif — Structure de pratique OU Revendeur"
        " (douilles usagées)",
    ),
]

# ---------------------------------------------------------------------------
# QCM — Étape 3 : Version de l'info-tri
# ---------------------------------------------------------------------------
VERSION_CHOICES = [
    ("redigee", "Version rédigée — avec le texte d'en-tête"),
    ("semi_redigee", "Version semi-rédigée — sans texte d'en-tête"),
]

# ---------------------------------------------------------------------------
# Texte d'en-tête du cartouche produit (version rédigée uniquement)
# ---------------------------------------------------------------------------
TEXTE_PRODUIT_BY_TYPE = {
    "asl_general": "CET ARTICLE SE TRIE",
    "gros_asl":    "CET ARTICLE SE TRIE",
    "epi":         "CET ARTICLE SE TRIE",
    "chasse_tir":  "LES DOUILLES USAGÉES SE TRIENT",
}

# ---------------------------------------------------------------------------
# SVG templates des labels complets (signalétique + FR + destinations)
# Un SVG par combinaison de destinations
# → À adapter si le produit contient un champ texte dynamique (nom_produit)
# ---------------------------------------------------------------------------
DEST_COMBO_SVG_TEMPLATES = {
    "asl_general": "ui/components/infotri_asl/svg/dest-combo-1.html",
    "gros_asl":    "ui/components/infotri_asl/svg/dest-combo-2.html",
    "epi":         "ui/components/infotri_asl/svg/dest-combo-3.html",
    "chasse_tir":  "ui/components/infotri_asl/svg/dest-combo-4.html",
}

# ---------------------------------------------------------------------------
# Libellés courts des destinations (pour aria-labels, radio buttons)
# ---------------------------------------------------------------------------
DEST_COMBO_LABELS = {
    "asl_general": "Association OU Magasin OU Déchèterie",
    "gros_asl":    "Association OU Reprise à domicile OU Déchèterie",
    "epi":         "Magasin OU Déchèterie",
    "chasse_tir":  "Structure de pratique OU Revendeur",
}

# ---------------------------------------------------------------------------
# "Privilégiez la réparation ou le don" — affiché sauf pour chasse_tir
# ---------------------------------------------------------------------------
AVEC_CONSEIL_REPARATION_BY_TYPE = {
    "asl_general": True,
    "gros_asl":    True,
    "epi":         True,
    "chasse_tir":  False,
}
