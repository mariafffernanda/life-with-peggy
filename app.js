/* Language toggle, scroll state for the top bar, and reveal-on-scroll. */
(function () {
  "use strict";

  var root = document.documentElement;
  var STORAGE_KEY = "pv-lang";

  /* ── Language ─────────────────────────────────────── */
  function setLang(lang) {
    root.dataset.lang = lang;
    root.setAttribute("lang", lang);
    try { localStorage.setItem(STORAGE_KEY, lang); } catch (e) { /* private mode */ }
  }

  var saved;
  try { saved = localStorage.getItem(STORAGE_KEY); } catch (e) { saved = null; }
  if (saved === "en" || saved === "es") {
    setLang(saved);
  } else if ((navigator.language || "").toLowerCase().indexOf("es") === 0) {
    setLang("es");
  }

  var toggle = document.getElementById("langtoggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      setLang(root.dataset.lang === "es" ? "en" : "es");
    });
  }

  /* ── Top bar background once the hero is behind us ── */
  var topbar = document.querySelector(".topbar");
  var hero = document.querySelector(".hero");
  if (topbar && hero && "IntersectionObserver" in window) {
    new IntersectionObserver(function (entries) {
      topbar.dataset.scrolled = String(!entries[0].isIntersecting);
    }, { rootMargin: "-70% 0px 0px 0px" }).observe(hero);
  }

  /* ── Reveal on scroll ─────────────────────────────── */
  var reveals = document.querySelectorAll(".reveal");
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (reduced || !("IntersectionObserver" in window)) {
    Array.prototype.forEach.call(reveals, function (el) { el.classList.add("is-in"); });
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-in");
        observer.unobserve(entry.target);
      }
    });
  }, { rootMargin: "0px 0px -12% 0px", threshold: 0.08 });

  Array.prototype.forEach.call(reveals, function (el) { observer.observe(el); });
})();
