/**
 * Script d'embed du configurateur Info-tri ASL.
 * Inséré via <script src=".../infotri-asl/configurateur.js">
 *
 * Crée une iframe pointant vers /infotri-asl/ (le configurateur complet)
 * et l'insère à la place du script tag.
 */
import iFrameResize from "iframe-resizer/js/iframeResizer";

(function () {
  const scripts = document.querySelectorAll<HTMLScriptElement>(
    'script[src*="infotri-asl/configurateur.js"]'
  );

  scripts.forEach((script) => {
    const baseUrl = script.src.replace("/infotri-asl/configurateur.js", "");

    const iframe = document.createElement("iframe");
    iframe.src = `${baseUrl}/infotri-asl/?iframe=true`;
    iframe.style.border = "none";
    iframe.style.width = "1px";
    iframe.style.minWidth = "100%";
    iframe.setAttribute("scrolling", "no");
    iframe.setAttribute("title", "Configurateur Info-tri ASL");

    script.parentNode?.insertBefore(iframe, script);
    script.remove();

    iFrameResize({ checkOrigin: false }, iframe);
  });
})();
