/* Native details and .bib downloads work without JavaScript. */
(() => {
  "use strict";

  if (!navigator.clipboard || !navigator.clipboard.writeText) return;

  document.querySelectorAll(".bibtex").forEach((details) => {
    const button = details.querySelector(".bibtex-copy");
    const code = details.querySelector("code");
    const status = details.querySelector(".bibtex-status");
    if (!button || !code || !status) return;

    button.hidden = false;
    button.addEventListener("click", async () => {
      button.disabled = true;
      status.textContent = "";
      try {
        await navigator.clipboard.writeText(code.textContent.trim());
        status.textContent = "Copied to clipboard.";
      } catch (error) {
        status.textContent = "Copy unavailable. Select the citation or download the .bib file.";
      } finally {
        button.disabled = false;
      }
    });
    details.addEventListener("toggle", () => {
      if (!details.open) status.textContent = "";
    });
  });
})();
