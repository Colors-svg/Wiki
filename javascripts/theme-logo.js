/* Wiki SIIU — logo según esquema de color.
 * Regla de marca: escudo verde #026937 sobre fondos claros,
 * blanco puro sobre fondos oscuros. Material guarda el esquema
 * en data-md-color-scheme del <body>.
 */
(function () {
  'use strict';
  var GREEN = 'assets/logo-udea.svg';
  var WHITE = 'assets/logo-udea-blanco.svg';

  function currentScheme() {
    var b = document.body;
    return (b && b.getAttribute('data-md-color-scheme')) || 'default';
  }

  function syncLogo() {
    var img = document.querySelector('.md-header__button.md-logo img');
    if (!img) return;
    var want = currentScheme() === 'slate' ? WHITE : GREEN;
    var cur = img.getAttribute('src') || '';
    if (cur.slice(-want.length) !== want) {
      img.setAttribute('src', want);
    }
  }

  function boot() {
    syncLogo();
    if (typeof MutationObserver !== 'undefined') {
      var scheduled = false;
      var obs = new MutationObserver(function () {
        if (scheduled) return;
        scheduled = true;
        var run = function () {
          scheduled = false;
          syncLogo();
        };
        if (typeof requestAnimationFrame === 'function') {
          requestAnimationFrame(run);
        } else {
          run();
        }
      });
      obs.observe(document.documentElement, {
        childList: true,
        subtree: true,
        attributes: true,
        attributeFilter: ['data-md-color-scheme']
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
