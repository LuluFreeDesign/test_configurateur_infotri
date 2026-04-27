/**
 * Script d'embed Info-tri ASL.
 * Inséré via <script src=".../infotri-asl/iframe.js" data-config="...">
 *
 * Crée une iframe pointant vers /infotri-asl/embed?{config}
 * et l'insère à la place du script tag.
 */
import iFrameResize from "iframe-resizer/js/iframeResizer";

(function () {
  const scripts = document.querySelectorAll<HTMLScriptElement>(
    'script[src*="infotri-asl/iframe.js"]'
  );

  scripts.forEach((script) => {
    const config = script.getAttribute("data-config") ?? "";
    const baseUrl = script.src.replace("/infotri-asl/iframe.js", "");

    const wrapper = document.createElement("div");
    wrapper.style.display = "inline-block";
    wrapper.style.maxWidth = "100%";

    const iframe = document.createElement("iframe");
    iframe.src = `${baseUrl}/infotri-asl/embed?${config}`;
    iframe.style.border = "none";
    iframe.style.width = "1px";
    iframe.style.minWidth = "100%";
    iframe.setAttribute("scrolling", "no");
    iframe.setAttribute("title", "Info-tri Articles de Sports et Loisirs");

    wrapper.appendChild(iframe);
    script.parentNode?.insertBefore(wrapper, script);
    script.remove();

    iFrameResize({ checkOrigin: false }, iframe);
  });
})();
