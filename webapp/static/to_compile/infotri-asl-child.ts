/**
 * Script child pour l'iframe Info-tri ASL.
 * Utilise iframe-resizer pour adapter la hauteur de l'iframe au contenu.
 */
import { IFrameComponent } from "iframe-resizer";

declare global {
  interface Window {
    iFrameResizer: IFrameComponent;
  }
}

window.iFrameResizer = {
  onReady() {
    document.body.style.overflow = "hidden";
  },
};
