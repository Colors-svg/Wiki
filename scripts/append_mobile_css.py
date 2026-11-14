import os

mobile_css = """

/* --------------------------------------------------------------------------
   Experiencia Movil y Drawer Lateral Enriquecido (UdeA)
   -------------------------------------------------------------------------- */
@media screen and (max-width: 76.2em) {
  /* Cabecera movil con elevacion y borde institucional */
  .md-header {
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.2) !important;
    border-bottom: 2px solid #026937 !important;
  }

  /* Drawer movil (menu hamburguesa) */
  .md-sidebar--primary .md-sidebar__scrollwrap {
    background: var(--card-bg) !important;
  }

  /* Cabecera del drawer movil con degradado institucional */
  .md-nav--primary .md-nav__title[for="__drawer"] {
    background: linear-gradient(135deg, #026937 0%, #112B1B 100%) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    padding: 1.2rem 1.1rem !important;
    font-size: 0.95rem !important;
    border-bottom: 3px solid #8DC63F !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25) !important;
  }

  /* Enlaces de navegacion movil: espaciado tactil ergonomico */
  .md-nav--primary .md-nav__link {
    padding: 0.65rem 1rem !important;
    margin: 0.15rem 0.5rem !important;
    border-radius: 6px !important;
    font-size: 0.88rem !important;
    transition: background-color 0.2s ease, color 0.2s ease !important;
  }

  /* Estado activo en navegacion movil */
  .md-nav--primary .md-nav__item--active > .md-nav__link {
    background: rgba(2, 105, 55, 0.14) !important;
    color: #8DC63F !important;
    font-weight: 600 !important;
    border-left: 3px solid #8DC63F !important;
  }

  [data-md-color-scheme="default"] .md-nav--primary .md-nav__item--active > .md-nav__link {
    background: rgba(2, 105, 55, 0.08) !important;
    color: #026937 !important;
    border-left: 3px solid #026937 !important;
  }

  /* Separadores sutiles entre secciones mayores */
  .md-nav--primary > .md-nav__list > .md-nav__item {
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  }
  [data-md-color-scheme="default"] .md-nav--primary > .md-nav__list > .md-nav__item {
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  }

  /* Botones de accion movil (buscar, menu, tema) */
  .md-header__button {
    padding: 0.4rem !important;
    border-radius: 8px !important;
    transition: transform 0.15s ease !important;
  }
  .md-header__button:active {
    transform: scale(0.92);
  }
}
"""

with open('docs/stylesheets/wiki.css', 'a', encoding='utf-8') as f:
    f.write(mobile_css)

print("Reglas moviles agregadas exitosamente.")
