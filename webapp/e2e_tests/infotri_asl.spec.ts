import { expect, test } from "@playwright/test";

const BASE_URL = process.env.BASE_URL ?? "http://localhost:8000";

test.describe("Configurateur Info-tri ASL", () => {

  test("affiche l'état vide sans sélection", async ({ page }) => {
    await page.goto(`${BASE_URL}/infotri-asl/`);
    await expect(page.getByText("Sélectionnez un type de produit")).toBeVisible();
  });

  const typesProduits = [
    {
      key: "asl_general",
      label: "Article de sport ou loisir",
      texteAttendu: "CET ARTICLE SE TRIE",
    },
    {
      key: "gros_asl",
      label: "Gros article de sport",
      texteAttendu: "CET ARTICLE SE TRIE",
    },
    {
      key: "epi",
      label: "Équipement de protection individuelle",
      texteAttendu: "CET ARTICLE SE TRIE",
    },
    {
      key: "chasse_tir",
      label: "Équipement de chasse et tir sportif",
      texteAttendu: "LES DOUILLES USAGÉES SE TRIENT",
    },
  ];

  for (const { key, label, texteAttendu } of typesProduits) {
    test(`affiche le bon texte produit pour : ${label}`, async ({ page }) => {
      await page.goto(
        `${BASE_URL}/infotri-asl/?type_produit=${key}&version=redigee`
      );
      await expect(page.getByText(texteAttendu)).toBeVisible();
    });
  }

  test("affiche le nom du produit dans l'aperçu", async ({ page }) => {
    await page.goto(
      `${BASE_URL}/infotri-asl/?type_produit=asl_general&nom_produit=v%C3%A9lo&version=redigee`
    );
    await expect(page.getByText("vélo")).toBeVisible();
  });

  test("n'affiche pas le conseil réparation pour chasse_tir", async ({ page }) => {
    await page.goto(
      `${BASE_URL}/infotri-asl/?type_produit=chasse_tir&nom_produit=douille&version=redigee`
    );
    await expect(
      page.getByText("Privilégiez la réparation ou le don")
    ).not.toBeVisible();
  });

  test("génère le code d'intégration", async ({ page }) => {
    await page.goto(
      `${BASE_URL}/infotri-asl/?type_produit=asl_general&nom_produit=raquette&version=redigee&show_code=true`
    );
    await expect(page.getByText("infotri-asl/iframe.js")).toBeVisible();
    await expect(page.getByText("type_produit=asl_general")).toBeVisible();
    await expect(page.getByText("nom_produit=raquette")).toBeVisible();
  });

  test("version semi-rédigée ne montre pas le texte d'en-tête", async ({ page }) => {
    await page.goto(
      `${BASE_URL}/infotri-asl/?type_produit=asl_general&nom_produit=v%C3%A9lo&version=semi_redigee`
    );
    await expect(page.getByText("CET ARTICLE SE TRIE")).not.toBeVisible();
    await expect(page.getByText("vélo")).toBeVisible();
  });

  test("affiche le SVG de destination pour l'aperçu embed", async ({ page }) => {
    await page.goto(
      `${BASE_URL}/infotri-asl/embed?type_produit=epi&nom_produit=casque&version=redigee`
    );
    await expect(page.locator("svg")).toBeVisible();
  });
});
