/* Wiki SIIU — Botón "Ampliar" para diagramas Mermaid.
 * Sin dependencias. Compatible con navigation.instant de Material.
 */
(function () {
  'use strict';

  var MIN_ZOOM = 0.5;
  var MAX_ZOOM = 2.5;
  var STEP = 0.25;

  function hasZoomButton(box) {
    var kids = box.children;
    for (var i = 0; i < kids.length; i++) {
      if (kids[i].className === 'diagram-zoom-btn') return true;
    }
    return false;
  }

  function initDiagramZoom(scope) {
    var root = scope || document;
    var boxes = root.querySelectorAll
      ? root.querySelectorAll('.mermaid')
      : [];
    boxes.forEach(function (box) {
      // Sin flags persistentes: el render de Mermaid reemplaza el
      // innerHTML y puede borrar el botón; si falta, se repone.
      if (hasZoomButton(box)) return;
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'diagram-zoom-btn';
      btn.textContent = '⛶ Ampliar';
      btn.setAttribute('aria-label', 'Ampliar diagrama en ventana grande');
      btn.addEventListener('click', function (ev) {
        ev.stopPropagation();
        openLightbox(box);
      });
      box.appendChild(btn);
    });
  }

  function openLightbox(box) {
    var pageTitle = document.querySelector('.md-content h1');
    var title = pageTitle ? pageTitle.textContent.trim() : 'Diagrama';

    var dlg = document.createElement('dialog');
    dlg.className = 'diagram-lightbox';
    dlg.setAttribute('aria-label', 'Diagrama ampliado: ' + title);

    var head = document.createElement('div');
    head.className = 'diagram-lightbox-head';

    var name = document.createElement('strong');
    name.textContent = title;

    var actions = document.createElement('div');
    actions.className = 'diagram-lightbox-actions';

    var zoom = 1;
    var scaler = document.createElement('div');
    scaler.className = 'diagram-lightbox-scaler';

    var btnOut = document.createElement('button');
    btnOut.type = 'button';
    btnOut.textContent = 'A−';
    btnOut.setAttribute('aria-label', 'Reducir zoom');

    var btnIn = document.createElement('button');
    btnIn.type = 'button';
    btnIn.textContent = 'A+';
    btnIn.setAttribute('aria-label', 'Aumentar zoom');

    function applyZoom() {
      scaler.style.transform = 'scale(' + zoom + ')';
    }
    btnOut.addEventListener('click', function () {
      zoom = Math.max(MIN_ZOOM, +(zoom - STEP).toFixed(2));
      applyZoom();
    });
    btnIn.addEventListener('click', function () {
      zoom = Math.min(MAX_ZOOM, +(zoom + STEP).toFixed(2));
      applyZoom();
    });

    var btnClose = document.createElement('button');
    btnClose.type = 'button';
    btnClose.className = 'diagram-lightbox-close';
    btnClose.textContent = '✕ Cerrar';
    btnClose.addEventListener('click', function () {
      dlg.close();
    });

    actions.appendChild(btnOut);
    actions.appendChild(btnIn);
    actions.appendChild(btnClose);
    head.appendChild(name);
    head.appendChild(actions);

    var body = document.createElement('div');
    body.className = 'diagram-lightbox-body';
    var clone = box.cloneNode(true);
    clone.removeAttribute('id');
    var oldBtn = clone.querySelector('.diagram-zoom-btn');
    if (oldBtn) oldBtn.remove();
    scaler.appendChild(clone);
    body.appendChild(scaler);

    dlg.appendChild(head);
    dlg.appendChild(body);
    document.body.appendChild(dlg);

    dlg.addEventListener('click', function (ev) {
      if (ev.target === dlg) dlg.close();
    });
    dlg.addEventListener('close', function () {
      dlg.remove();
    });

    if (typeof dlg.showModal === 'function') {
      dlg.showModal();
    } else {
      dlg.setAttribute('open', '');
    }
  }

  function boot() {
    initDiagramZoom(document);
    // navigation.instant de Material reemplaza el <body> sin re-ejecutar
    // este script: el observador cubre esos cambios sin depender de
    // globales internos del bundle (document$ está minificado).
    if (typeof MutationObserver !== 'undefined') {
      var scheduled = false;
      var obs = new MutationObserver(function () {
        if (scheduled) return;
        scheduled = true;
        var run = function () {
          scheduled = false;
          initDiagramZoom(document);
        };
        if (typeof requestAnimationFrame === 'function') {
          requestAnimationFrame(run);
        } else {
          run();
        }
      });
      obs.observe(document.documentElement, {
        childList: true,
        subtree: true
      });
    }
  }

  if (
    typeof window.document$ !== 'undefined' &&
    window.document$ &&
    typeof window.document$.subscribe === 'function'
  ) {
    window.document$.subscribe(function () {
      initDiagramZoom(document);
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
