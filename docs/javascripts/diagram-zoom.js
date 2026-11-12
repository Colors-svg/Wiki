/* Wiki SIIU — Botón "Ampliar" para diagramas Mermaid.
 * Sin dependencias. Compatible con navigation.instant de Material.
 * Nota: Material renderiza Mermaid dentro de un Shadow DOM CERRADO
 * (el <pre> se reemplaza por un div.mermaid anfitrión). Por eso el botón
 * NO va dentro del diagrama (sería invisible sin <slot>), sino en un
 * envoltorio hermano, y el modal MUEVE el nodo real (con su shadow).
 */
(function () {
  'use strict';

  var MIN_ZOOM = 0.5;
  var MAX_ZOOM = 2.5;
  var STEP = 0.25;

  function wrapOf(box) {
    var p = box.parentNode;
    return p && p.classList && p.classList.contains('diagram-zoom-wrap') ? p : null;
  }

  function hasZoomButton(box) {
    var wrap = wrapOf(box);
    return !!(wrap && wrap.querySelector(':scope > .diagram-zoom-btn'));
  }

  function initOne(box) {
    if (box.closest && box.closest('dialog.diagram-lightbox')) return;
    if (hasZoomButton(box)) return;
    var wrap = wrapOf(box);
    if (!wrap) {
      wrap = document.createElement('div');
      wrap.className = 'diagram-zoom-wrap';
      box.parentNode.insertBefore(wrap, box);
      wrap.appendChild(box);
    }
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'diagram-zoom-btn';
    btn.innerHTML = '<svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M16.5 16.5 21 21"/></svg><span>Ampliar</span>';
    btn.setAttribute('aria-label', 'Ampliar diagrama en ventana grande');
    btn.addEventListener('click', function (ev) {
      ev.stopPropagation();
      openLightbox(box);
    });
    wrap.appendChild(btn);
  }

  function initDiagramZoom(scope) {
    var root = scope || document;
    var boxes = root.querySelectorAll
      ? root.querySelectorAll('.mermaid')
      : [];
    boxes.forEach(initOne);
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
    btnOut.textContent = 'A-';
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
    btnClose.textContent = '× Cerrar';
    btnClose.addEventListener('click', function () {
      dlg.close();
    });

    actions.appendChild(btnOut);
    actions.appendChild(btnIn);
    actions.appendChild(btnClose);
    head.appendChild(name);
    head.appendChild(actions);

    // Mover el nodo real (con su shadow) al modal y devolverlo al cerrar.
    var placeholder = document.createComment('diagrama-ampliado');
    box.parentNode.insertBefore(placeholder, box);
    scaler.appendChild(box);

    var body = document.createElement('div');
    body.className = 'diagram-lightbox-body';
    body.appendChild(scaler);

    dlg.appendChild(head);
    dlg.appendChild(body);
    document.body.appendChild(dlg);

    function restore() {
      if (placeholder.parentNode) {
        placeholder.parentNode.insertBefore(box, placeholder);
        placeholder.remove();
      }
    }

    dlg.addEventListener('click', function (ev) {
      if (ev.target === dlg) dlg.close();
    });
    dlg.addEventListener('close', function () {
      restore();
      dlg.remove();
      initDiagramZoom(document);
    });

    if (typeof dlg.showModal === 'function') {
      dlg.showModal();
    } else {
      dlg.setAttribute('open', '');
    }
  }

  function boot() {
    initDiagramZoom(document);
    // navigation.instant reemplaza el <body> sin re-ejecutar este script:
    // el observador cubre esos cambios y los re-renders de Mermaid.
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
