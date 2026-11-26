/* Wiki SIIU — logo según esquema de color.
 * Regla de marca: escudo verde #026937 sobre fondos claros,
 * blanco puro sobre fondos oscuros. Material guarda el esquema
 * en data-md-color-scheme del <body>.
 */
(function () {
  'use strict';
  var GREEN = 'logo-udea.svg';
  var WHITE = 'logo-udea-blanco.svg';

  function withFile(src, file) {
    var i = src.lastIndexOf('/');
    return (i < 0 ? '' : src.slice(0, i + 1)) + file;
  }

  function currentScheme() {
    var b = document.body;
    return (b && b.getAttribute('data-md-color-scheme')) || 'default';
  }

  function syncLogo() {
    var want = currentScheme() === 'slate' ? WHITE : GREEN;
    var imgs = document.querySelectorAll('.md-header__button.md-logo img');
    for (var k = 0; k < imgs.length; k++) {
      var cur = imgs[k].getAttribute('src') || '';
      if (cur.slice(-want.length) !== want) {
        imgs[k].setAttribute('src', withFile(cur, want));
      }
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
