# -*- coding: utf-8 -*-
"""
Generador de páginas del sitio del Consejo Nacional de Mujeres del Perú.
Uso:  python3 _build/build.py          (desde la raíz del proyecto)
Escribe los .html en la raíz a partir de los bloques definidos aquí.
"""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import hashlib
def _ver(rel_path):
    try:
        return hashlib.md5(open(os.path.join(ROOT, rel_path), "rb").read()).hexdigest()[:8]
    except OSError:
        return "1"
CSS_V = _ver("css/styles.css"); JS_V = _ver("js/main.js")
SITE = "https://consejonacionaldemujeresdelperu.com/"
FB = "https://www.facebook.com/p/Consejo-Nacional-de-Mujeres-del-Per%C3%BA-100068176325426/"
TEL = "+51 990 457 014"; TEL_LINK = "+51990457014"; MAIL = "cnmp031923@gmail.com"

def head(title, desc, path, extra="", rel="", og_image=None, og_type="website"):
    og_image = og_image or (SITE + "img/og-image.jpg")
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="author" content="Consejo Nacional de Mujeres del Perú">
    <link rel="canonical" href="{SITE}{path}">
    <link rel="alternate" type="application/rss+xml" title="Noticias · Consejo Nacional de Mujeres del Perú" href="{SITE}feed.xml">
    <meta name="theme-color" content="#0f2558">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="{og_type}">
    <meta property="og:url" content="{SITE}{path}">
    <meta property="og:locale" content="es_PE">
    <meta property="og:site_name" content="Consejo Nacional de Mujeres del Perú">
    <meta property="og:image" content="{og_image}">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="icon" type="image/png" sizes="32x32" href="{rel}img/favicon-32.png">
    <link rel="icon" type="image/png" sizes="64x64" href="{rel}img/favicon-64.png">
    <link rel="apple-touch-icon" href="{rel}img/apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="{rel}css/styles.css?v={CSS_V}">
{extra}</head>
<body>
'''

SCHEMA = '''    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "NGO",
        "name": "Consejo Nacional de Mujeres del Perú",
        "alternateName": "CNMP",
        "url": "https://consejonacionaldemujeresdelperu.com/",
        "logo": "https://consejonacionaldemujeresdelperu.com/img/logo-512.png",
        "foundingDate": "1923-03-03",
        "foundingLocation": { "@type": "Place", "name": "Lima, Perú" },
        "memberOf": { "@type": "Organization", "name": "Consejo Internacional de Mujeres (ICW-CIF)", "url": "https://www.icw-cif.com/" },
        "description": "Asociación civil sin fines de lucro fundada en 1923, afiliada al Consejo Internacional de Mujeres desde 1926, que promueve los derechos, la igualdad y la superación de la mujer y la familia en el Perú.",
        "address": { "@type": "PostalAddress", "addressLocality": "Lima", "addressCountry": "PE" },
        "telephone": "+51990457014",
        "email": "cnmp031923@gmail.com",
        "sameAs": ["https://www.facebook.com/p/Consejo-Nacional-de-Mujeres-del-Per%C3%BA-100068176325426/"]
    }
    </script>
'''

NAV = [("index.html", "Inicio"), ("nosotros.html", "Nosotros"), ("que-hacemos.html", "Qué hacemos"), ("noticias.html", "Noticias"), ("participa.html", "Participa"), ("contacto.html", "Contacto")]

def header(rel=""):
    return f'''    <a class="skip-link" href="#contenido">Ir al contenido</a>

    <div class="topbar">
        <div class="container">
            <div class="topbar__info">
                <a href="tel:{TEL_LINK}"><i class="fas fa-phone"></i><span>{TEL}</span></a>
                <a href="mailto:{MAIL}"><i class="fas fa-envelope"></i><span>{MAIL}</span></a>
                <a href="{rel}contacto.html"><i class="fas fa-location-dot"></i><span>Lima, Perú</span></a>
            </div>
            <div class="topbar__social">
                <a href="{FB}" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                <a href="https://wa.me/51990457014" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
            </div>
        </div>
    </div>

    <header class="header">
        <div class="container">
            <a class="brand" href="{rel}index.html" aria-label="Consejo Nacional de Mujeres del Perú, inicio">
                <img src="{rel}img/logo-192.png" alt="Escudo del Consejo Nacional de Mujeres del Perú" width="58" height="58">
                <span class="brand__text">
                    <span class="brand__name">Consejo Nacional de Mujeres del Perú</span>
                    <span class="brand__tag">Desde 1923</span>
                </span>
            </a>
            <button class="nav-toggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="menu">
                <span></span><span></span><span></span>
            </button>
            <nav class="nav" id="menu" aria-label="Principal">
                <ul class="nav__list">
''' + "".join(f'                    <li><a href="{rel}{h}">{l}</a></li>\n' for h, l in NAV) + f'''                    <li class="nav__cta"><a class="btn btn--primary btn--sm" href="{rel}participa.html">Afíliate</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main id="contenido">
'''

def footer(rel=""):
    return f'''    </main>

    <footer class="footer">
        <div class="container">
            <div class="footer__grid">
                <div>
                    <a class="brand" href="{rel}index.html">
                        <img src="{rel}img/logo-192.png" alt="" width="58" height="58">
                        <span class="brand__text">
                            <span class="brand__name">Consejo Nacional de Mujeres del Perú</span>
                            <span class="brand__tag">Desde 1923</span>
                        </span>
                    </a>
                    <p>Asociación civil sin fines de lucro fundada el 3 de marzo de 1923. Afiliada al Consejo Internacional de Mujeres desde 1926 y única representante de la mujer peruana ante el CIDEM y el Consejo Regional de Mujeres de las Américas.</p>
                    <div class="footer__social">
                        <a href="{FB}" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                        <a href="mailto:{MAIL}" aria-label="Correo electrónico"><i class="fas fa-envelope"></i></a>
                        <a href="https://wa.me/51990457014" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
                    </div>
                </div>
                <div>
                    <h4>Institución</h4>
                    <ul class="footer__links">
                        <li><a href="{rel}nosotros.html">Nosotros</a></li>
                        <li><a href="{rel}nosotros.html#historia">Historia</a></li>
                        <li><a href="{rel}nosotros.html#consejo-directivo">Consejo Directivo</a></li>
                        <li><a href="{rel}que-hacemos.html">Qué hacemos</a></li>
                        <li><a href="{rel}noticias.html">Noticias</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Enlaces</h4>
                    <ul class="footer__links">
                        <li><a href="{rel}participa.html#afiliacion">Afiliación</a></li>
                        <li><a href="{rel}participa.html#asociaciones">Asociaciones afiliadas</a></li>
                        <li><a href="{rel}participa.html#preguntas">Preguntas frecuentes</a></li>
                        <li><a href="{rel}contacto.html">Contacto</a></li>
                        <li><a href="{rel}creditos.html">Créditos fotográficos</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Contacto</h4>
                    <ul class="footer__contact">
                        <li><i class="fas fa-location-dot"></i><span>Lima, Perú</span></li>
                        <li><i class="fas fa-phone"></i><a href="tel:{TEL_LINK}">{TEL}</a></li>
                        <li><i class="fas fa-envelope"></i><a href="mailto:{MAIL}">{MAIL}</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="footer__bottom">
            <div class="container">
                <span>© <span data-year></span> Consejo Nacional de Mujeres del Perú. Todos los derechos reservados.</span>
                <span>Desarrollado por <a href="https://ciriacodeveloper.com" target="_blank" rel="noopener noreferrer">Ciriaco Developer</a></span>
            </div>
        </div>
    </footer>

    <button class="back-top" aria-label="Volver arriba"><i class="fas fa-chevron-up"></i></button>
    <script src="{rel}js/main.js?v={JS_V}"></script>
</body>
</html>
'''

def page_hero(title, text, img, crumb):
    return f'''        <section class="hero hero--page">
            <div class="hero__bg"><img src="{img}" alt="" fetchpriority="high"></div>
            <div class="container">
                <div class="hero__content">
                    <nav class="breadcrumb" aria-label="Ruta"><a href="index.html">Inicio</a><span>/</span><span>{crumb}</span></nav>
                    <h1>{title}</h1>
                    <p>{text}</p>
                </div>
            </div>
        </section>
'''

def cta(rel=""):
    return f'''        <section class="cta">
            <div class="container">
                <div>
                    <h2>Sé parte de una historia que sigue escribiéndose</h2>
                    <p>Afíliate como asociada, integra a tu asociación o apoya nuestras actividades. Cada mujer que se suma fortalece a todas.</p>
                </div>
                <div class="cta__actions">
                    <a class="btn btn--white" href="{rel}participa.html">Afíliate al Consejo</a>
                    <a class="btn btn--ghost" href="{rel}contacto.html">Escríbenos</a>
                </div>
            </div>
        </section>
'''

# ---------------------------------------------------------------- datos oficiales (estatuto)
FINES = [
    "Promover el reconocimiento y el respeto de los derechos de la persona y fomentar la eliminación de toda forma de discriminación por razón de nacimiento, sexo, raza, idioma o religión.",
    "Propiciar la igualdad de los derechos y responsabilidades del hombre y la mujer en todos los aspectos del quehacer humano.",
    "Fomentar en las mujeres del Perú la toma de conciencia de sus responsabilidades en el seno de la familia y la sociedad, prepararlas e incentivarlas a participar en la vida pública del país.",
    "Unir esfuerzos para desterrar toda forma de violencia y discriminación contra la mujer y el menor.",
    "Ejercer función conciliadora y otros medios alternativos de solución de conflictos, como la negociación y el arbitraje, así como ejercer función de capacitación de acuerdo con las leyes vigentes.",
    "Constituir centros de conciliación y capacitación extrajudicial, de educación y aprendizaje, consultorios jurídicos y botiquines médicos.",
    "Promover la constitución de microempresas de acuerdo con los fines y objetivos de la asociación.",
    "Reforzar el entendimiento y la comprensión mutua de las personas elevando su nivel cultural.",
]
OBJETIVOS = [
    ("fa-arrow-trend-up", "Superación de la persona", "Promover la superación individual y colectiva de la persona y la sociedad, el ejercicio de sus derechos y el cumplimiento de sus deberes."),
    ("fa-people-line", "Congresos y foros", "Promover congresos, seminarios, foros, mesas redondas y otros eventos, en coordinación con filiales, asociaciones afiliadas, universidades e instituciones afines."),
    ("fa-earth-americas", "Representación", "Llevar la representación de la mujer peruana a los certámenes nacionales e internacionales donde se debatan asuntos relacionados con los fines del CNMP."),
    ("fa-handshake", "Convenios y alianzas", "Celebrar acuerdos, convenios y contratos, aceptar donaciones y recibir legados de personas naturales o jurídicas, públicas o privadas, nacionales o internacionales."),
    ("fa-book-open", "Publicaciones", "Publicar libros, revistas, boletines y folletos, y hacer uso de los medios de comunicación social para los fines de la institución."),
]
COMISIONES = [
    ("fa-graduation-cap", "Educación, medios de comunicación social, profesiones y ocupación"),
    ("fa-masks-theater", "Cultura"),
    ("fa-heart-pulse", "Salud integral, bienestar social y proyección a la comunidad"),
    ("fa-people-roof", "Desarrollo de la persona, el menor, la mujer, la familia y el adulto mayor"),
    ("fa-scale-balanced", "Legislación y derechos humanos"),
    ("fa-leaf", "Ecología"),
    ("fa-hand-holding-heart", "Ética, valores y moral de la persona y la sociedad"),
    ("fa-mountain-sun", "Turismo, artesanía y folklore"),
    ("fa-globe", "Relaciones nacionales e internacionales"),
]
CONSEJO = [
    ("Presidenta", "María Amelia de la Mercedes Asenjo Azpilcueta"),
    ("1.ª Vicepresidenta", "Vilma Alicia Rodríguez Montero vda. de Ruiz"),
    ("2.ª Vicepresidenta", "Rocío Milagros Esquivel García"),
    ("Tesorera", "Carmen Graciela Montalva Rajkovic"),
    ("Pro Tesorera", "Sofía Milagritos Cuadra Flores"),
    ("Secretaria General", "Marina Rosalva Vásquez Hurtado"),
    ("Secretaria de Actas", "Patricia Avelina Salazar Ramírez"),
    ("Pro Secretaria", "Vilma Violeta Ruiz Rodríguez"),
    ("Vocal de Finanzas", "Ana María Cedeño Alvarado"),
    ("Vocal de Relaciones Públicas", "Carolina Melchora Martínez Velezmoro"),
    ("Vocal de Cultura", "Teresa Sebastiana Arbaiza Fernández"),
    ("Vocal de Comunicaciones", "Vicenta Bárbara Sandoval Samaniego"),
]
TIMELINE = [
    ("1888", "Nace el Consejo Internacional de Mujeres", "Se funda en Washington el Consejo Internacional de Mujeres, primera organización femenina de alcance mundial, hoy con sede en París, que inspirará la creación de consejos nacionales en todos los continentes."),
    ("1914", "Evolución Femenina", "María Jesús Alvarado Rivera funda Evolución Femenina, la primera organización feminista del Perú, dedicada a la cultura y los derechos de la mujer."),
    ("1923", "Fundación del Consejo", "El 3 de marzo, durante la visita a Lima de Carrie Chapman Catt, se constituye el Consejo Nacional de Mujeres del Perú. María Jesús Alvarado asume la secretaría y Mercedes Gallagher de Parks la presidencia del comité directivo."),
    ("1924", "II Conferencia Panamericana de Mujeres", "En diciembre, Lima es sede de la Segunda Conferencia Panamericana de Mujeres, presidida por la presidenta del Consejo. Ese mismo año el Consejo debate la reforma del Código Civil para reconocer la igualdad de la mujer ante la ley."),
    ("1925", "Vida institucional", "El comité directivo sesiona en el Liceo Grau bajo la presidencia de Mercedes Gallagher de Parks, con Amalia Puga de Losada, Ester Festini de Ramos Ocampo, Luisa Dammert, Elvira García y García y Elvira Rodrigues Lorente."),
    ("1926", "Afiliación al Consejo Internacional de Mujeres", "El Consejo se afilia al Consejo Internacional de Mujeres (CIDEM), con sede en París, manteniendo su autonomía interna. Desde entonces es la única institución que representa a la mujer peruana ante el CIDEM y ante el Consejo Regional de Mujeres de las Américas (CRA)."),
    ("1955", "Voto femenino", "El 7 de septiembre se promulga la Ley 12391, que reconoce a las peruanas el derecho a elegir y ser elegidas, una causa que el Consejo impulsó desde sus orígenes. En 1956 las mujeres votan por primera vez en elecciones nacionales."),
    ("1963", "Primera alcaldesa de Lima", "Anita Fernandini de Naranjo, presidenta vitalicia del Consejo, es elegida alcaldesa de Lima, la primera mujer en ocupar el cargo en la historia de la capital."),
    ("1969", "Homenaje a la fundadora", "El Consejo reconoce a María Jesús Alvarado Rivera como «la primera adalid moderna de los derechos de la mujer en el Perú»."),
    ("1988", "Plaza del Rosario", "El Consejo lidera la construcción de la Plaza del Rosario, en Jesús María, con motivo de la segunda visita de San Juan Pablo II al Perú. Es inaugurada el 13 de mayo y bendecida por el Papa el 14 de mayo de 1988."),
    ("2023", "Centenario", "El Consejo Nacional de Mujeres del Perú cumple cien años de vida institucional y renueva su compromiso con las nuevas generaciones de mujeres peruanas."),
    ("2026", "Consejo Directivo 2025–2027", "Juramenta en ceremonia solemne el Consejo Directivo para el periodo 2025–2027, presidido por María Amelia Asenjo Azpilcueta."),
]
PIONERAS = [
    ("maria-jesus-alvarado.jpg", "Fundadora · 1878–1971", "María Jesús Alvarado Rivera", "Educadora, periodista y pionera del feminismo peruano. En 1911 reclamó públicamente la igualdad de derechos civiles y políticos para la mujer. Fundó Evolución Femenina y, en 1923, el Consejo, del que fue secretaria. Fue encarcelada y desterrada en 1924 por su activismo."),
    ("mercedes-gallagher.jpg", "Presidenta fundadora · 1883–1950", "Mercedes Gallagher de Parks", "Escritora, crítica de arte y promotora cultural limeña. Presidió el comité directivo del Consejo en sus primeros años y es recordada como fundadora de la institución en 1923."),
    ("elvira-garcia.jpg", "Educadora · 1862–1951", "Elvira García y García", "Fundadora del Liceo Fanning y referente de la educación femenina en el Perú. Integró el comité directivo del Consejo y fue autora de obras pioneras sobre la mujer peruana."),
    ("angelica-palma.jpg", "Escritora · 1878–1935", "Angélica Palma", "Novelista y periodista, hija de Ricardo Palma. Vinculada al Consejo desde sus inicios, representó al Perú ante la asamblea general del Consejo Internacional de Mujeres."),
    ("carrie-chapman-catt.jpg", "Impulsora internacional · 1859–1947", "Carrie Chapman Catt", "Líder sufragista estadounidense y presidenta de la Alianza Internacional por el Sufragio de la Mujer. Su visita a Lima en 1923 fue el impulso para la fundación del Consejo."),
    (None, "Presidenta vitalicia", "Anita Fernandini de Naranjo", "Benefactora y dirigente social, presidenta vitalicia del Consejo. En 1963 se convirtió en la primera mujer elegida alcaldesa de Lima."),
]

def timeline_html(items, cls="tl-item reveal"):
    return "".join(f'<div class="{cls}"><div class="tl-item__year">{y}</div><div class="tl-item__card"><h3>{h}</h3><p>{p}</p></div></div>\n                    ' for y, h, p in items)

def pioneras_html(items):
    out = ""
    for img, role, name, text in items:
        media = (f'<div class="person__img"><img src="img/historia/{img}" alt="Retrato de {name}" loading="lazy"></div>' if img
                 else '<div class="person__img person__img--mono" aria-hidden="true"><span>AF</span></div>')
        out += f'''                    <article class="person reveal">
                        {media}
                        <div class="person__body">
                            <div class="person__role">{role}</div>
                            <h3>{name}</h3>
                            <p>{text}</p>
                        </div>
                    </article>
'''
    return out

def aims_html(items):
    return "".join(f'<div class="aim reveal"><p>{t}</p></div>\n                    ' for t in items)

def board_html():
    return "".join(f'<li><span>{r}</span><strong>{n}</strong></li>' for r, n in CONSEJO)

pages = {}

# ================================================================ INICIO
pages["index.html"] = dict(
    title="Consejo Nacional de Mujeres del Perú | Desde 1923",
    desc="El Consejo Nacional de Mujeres del Perú (CNMP) es una asociación civil sin fines de lucro fundada en Lima el 3 de marzo de 1923, afiliada al Consejo Internacional de Mujeres desde 1926, que promueve los derechos, la igualdad y la superación de la mujer peruana.",
    path="", schema=True,
    body=f'''        <section class="hero">
            <div class="hero__bg"><img src="img/fotos/hero.jpg" alt="" fetchpriority="high"></div>
            <div class="container">
                <div class="hero__content">
                    <span class="hero__badge"><i class="fas fa-award"></i> Fundado el 3 de marzo de 1923</span>
                    <h1>Más de un siglo impulsando la superación de la <em>mujer</em> y la familia peruana</h1>
                    <p>Somos una asociación civil sin fines de lucro, de carácter nacional, que reúne a ciudadanas y asociaciones comprometidas con los derechos, la igualdad y el desarrollo integral de la mujer y la familia en el Perú.</p>
                    <div class="btn-group">
                        <a class="btn btn--primary" href="nosotros.html">Conócenos <i class="fas fa-arrow-right"></i></a>
                        <a class="btn btn--ghost" href="participa.html">Quiero participar</a>
                    </div>
                </div>
            </div>
            <div class="hero__scroll">Descubre <i class="fas fa-chevron-down"></i></div>
        </section>

        <section class="stats">
            <div class="container">
                <div class="stats__grid reveal">
                    <div class="stat"><div class="stat__value">1923</div><div class="stat__label">Año de fundación en Lima</div></div>
                    <div class="stat"><div class="stat__value">1926</div><div class="stat__label">Afiliados al Consejo Internacional de Mujeres, con sede en París</div></div>
                    <div class="stat"><div class="stat__value">9</div><div class="stat__label">Comisiones permanentes de trabajo</div></div>
                    <div class="stat"><div class="stat__value">100<span>+</span></div><div class="stat__label">Años de trayectoria al servicio de la mujer peruana</div></div>
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <div class="split">
                    <div class="split__media split__media--wide reveal">
                        <img src="img/fotos/juramentacion-2026.jpg" alt="Integrantes del Consejo Directivo 2025–2027 en su ceremonia de juramentación" loading="lazy">
                        <div class="split__badge">
                            <strong>2025–2027</strong>
                            <span>Consejo Directivo juramentado en ceremonia solemne en 2026</span>
                        </div>
                    </div>
                    <div class="split__content reveal reveal-delay-1">
                        <span class="eyebrow">Quiénes somos</span>
                        <h2>La institución que representa a la mujer peruana desde 1923</h2>
                        <p>El Consejo Nacional de Mujeres del Perú (CNMP) es una asociación civil de carácter nacional y una organización no gubernamental sin fines de lucro, conformada por ciudadanas y asociaciones que se identifican con sus fines.</p>
                        <p>Desde 1926 está afiliado al Consejo Internacional de Mujeres (CIDEM), con sede en París, y es la única institución que representa a la mujer peruana ante el CIDEM y ante el Consejo Regional de Mujeres de las Américas (CRA).</p>
                        <ul class="checklist">
                            <li><i class="fas fa-circle-check"></i><span>Promueve los derechos de la persona y la igualdad entre hombres y mujeres.</span></li>
                            <li><i class="fas fa-circle-check"></i><span>No participa en actividades político partidarias y respeta las creencias de sus asociadas.</span></li>
                            <li><i class="fas fa-circle-check"></i><span>Respeta la independencia y autonomía de las asociaciones afiliadas.</span></li>
                        </ul>
                        <a class="btn btn--azul" href="nosotros.html">Conoce nuestra historia <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        </section>

        <section class="section section--crema">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Qué hacemos</span>
                    <h2>Nuestras líneas de acción</h2>
                    <p class="lead">Los fines y objetivos que establece nuestro estatuto se concretan en el trabajo de nueve comisiones permanentes.</p>
                </div>
                <div class="grid grid--4">
                    <article class="card card--num reveal" data-num="01">
                        <div class="card__icon"><i class="fas fa-scale-balanced"></i></div>
                        <h3>Derechos e igualdad</h3>
                        <p>Promovemos el respeto de los derechos de la persona, la igualdad entre hombres y mujeres y la eliminación de toda forma de violencia y discriminación.</p>
                        <a class="card__link" href="que-hacemos.html#derechos">Conocer más <i class="fas fa-arrow-right"></i></a>
                    </article>
                    <article class="card card--num reveal reveal-delay-1" data-num="02">
                        <div class="card__icon"><i class="fas fa-graduation-cap"></i></div>
                        <h3>Formación y participación</h3>
                        <p>Congresos, seminarios y foros que preparan e incentivan a las mujeres a participar en la vida pública del país.</p>
                        <a class="card__link" href="que-hacemos.html#formacion">Conocer más <i class="fas fa-arrow-right"></i></a>
                    </article>
                    <article class="card card--num reveal reveal-delay-2" data-num="03">
                        <div class="card__icon"><i class="fas fa-heart-pulse"></i></div>
                        <h3>Familia, salud y comunidad</h3>
                        <p>Acciones de bienestar social y proyección a la comunidad en favor de la mujer, el menor, la familia y el adulto mayor.</p>
                        <a class="card__link" href="que-hacemos.html#familia">Conocer más <i class="fas fa-arrow-right"></i></a>
                    </article>
                    <article class="card card--num reveal reveal-delay-3" data-num="04">
                        <div class="card__icon"><i class="fas fa-handshake-angle"></i></div>
                        <h3>Conciliación y servicios</h3>
                        <p>Función conciliadora, capacitación extrajudicial, consultorios jurídicos y promoción de microempresas.</p>
                        <a class="card__link" href="que-hacemos.html#conciliacion">Conocer más <i class="fas fa-arrow-right"></i></a>
                    </article>
                </div>
            </div>
        </section>

        <section class="section section--azul">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Nuestra historia</span>
                    <h2>Un siglo de historia junto a la mujer peruana</h2>
                    <p class="lead">De la lucha por el voto femenino a la Plaza del Rosario y al presente: hitos de una institución centenaria.</p>
                </div>
                <div class="timeline">
                    {timeline_html([TIMELINE[2], TIMELINE[5], TIMELINE[6], TIMELINE[9], TIMELINE[11]])}
                </div>
                <div class="text-center mt-32 reveal">
                    <a class="btn btn--white" href="nosotros.html#historia">Ver la historia completa <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>
        </section>

        <section class="section section--gris">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Noticias</span>
                    <h2>Actualidad del Consejo</h2>
                    <p class="lead">Ceremonias, actividades y novedades de la vida institucional.</p>
                </div>
                <div class="news-feature">
                    <a class="feature reveal" href="noticias/juramentacion-consejo-directivo-2025-2027.html">
                        <img src="img/fotos/juramentacion-2026.jpg" alt="Ceremonia de juramentación del Consejo Directivo 2025–2027" loading="lazy">
                        <span class="feature__badge">2026</span>
                        <div class="feature__body">
                            <span class="feature__tag">Institucional</span>
                            <h3>Juramentó el Consejo Directivo para el periodo 2025–2027</h3>
                            <p>En ceremonia solemne, las integrantes del nuevo Consejo Directivo, presidido por María Amelia Asenjo Azpilcueta, asumieron sus cargos conforme al estatuto.</p>
                            <span class="feature__link">Leer la nota <i class="fas fa-arrow-right"></i></span>
                        </div>
                    </a>
                    <div class="news-list">
                        <a class="news-item reveal reveal-delay-1" href="noticias/bodas-de-plata-doctorado-economia-unfv.html">
                            <div class="news-item__img"><img src="img/fotos/noticia-unfv-2026.jpg" alt="" loading="lazy" style="object-position: 30% center"></div>
                            <div class="news-item__body">
                                <span class="news-item__meta">7 nov 2026 · Presidencia</span>
                                <h3>Nuestra presidenta celebró las Bodas de Plata de su promoción doctoral en la UNFV</h3>
                                <span class="news-item__more">Leer más <i class="fas fa-arrow-right"></i></span>
                            </div>
                        </a>
                        <a class="news-item reveal reveal-delay-2" href="nosotros.html#consejo-directivo">
                            <div class="news-item__img news-item__img--mono"><i class="fas fa-users"></i></div>
                            <div class="news-item__body">
                                <span class="news-item__meta">Periodo 2025–2027 · Institución</span>
                                <h3>Conoce a las doce integrantes del nuevo Consejo Directivo</h3>
                                <span class="news-item__more">Ver el Consejo Directivo <i class="fas fa-arrow-right"></i></span>
                            </div>
                        </a>
                        <a class="news-item reveal reveal-delay-3" href="noticias/rezo-del-rosario-primeros-sabados.html">
                            <div class="news-item__img"><img src="img/fotos/plaza-del-rosario.jpg" alt="" loading="lazy"></div>
                            <div class="news-item__body">
                                <span class="news-item__meta">Primeros sábados · 5:00 p.m. · Actividad permanente</span>
                                <h3>Rezo del Rosario en la Plaza del Rosario, Jesús María</h3>
                                <span class="news-item__more">Leer más <i class="fas fa-arrow-right"></i></span>
                            </div>
                        </a>
                        <a class="btn btn--outline news-list__all reveal reveal-delay-3" href="noticias.html">Ver todas las noticias <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        </section>

''' + cta())

# ================================================================ NOSOTROS
pages["nosotros.html"] = dict(
    title="Nosotros e historia | Consejo Nacional de Mujeres del Perú",
    desc="Quiénes somos, fines, historia completa desde 1923, pioneras, emblemas, organización y Consejo Directivo 2025–2027 del Consejo Nacional de Mujeres del Perú.",
    path="nosotros.html",
    body=page_hero("Nosotros", "Más de un siglo de historia al servicio de la mujer peruana: quiénes somos, de dónde venimos y cómo nos organizamos.", "img/fotos/nosotros-hero.jpg", "Nosotros") + f'''
        <section class="section">
            <div class="container">
                <div class="split split--reverse">
                    <div class="split__media reveal">
                        <img src="img/fotos/sede-lima.jpg" alt="Plaza Mayor de Lima, ciudad sede del Consejo" loading="lazy">
                        <div class="split__badge">
                            <strong>Lima</strong>
                            <span>Domicilio institucional, con facultad de establecer filiales en todas las regiones</span>
                        </div>
                    </div>
                    <div class="split__content reveal reveal-delay-1">
                        <span class="eyebrow">Quiénes somos</span>
                        <h2>Reseña institucional</h2>
                        <p>El Consejo Nacional de Mujeres del Perú (CNMP) es una asociación civil de carácter nacional y persona jurídica de derecho privado, constituida conforme a las leyes de la República y conformada por ciudadanas y asociaciones que se identifican con sus fines. Es una organización no gubernamental (ONG) sin fines de lucro, fundada el 3 de marzo de 1923.</p>
                        <p>El CNMP está afiliado al Consejo Internacional de Mujeres (CIDEM), con sede en París, desde 1926, manteniendo autonomía en su organización interna y en su actividad a nivel nacional. Es la única institución que representa a la mujer peruana ante el CIDEM y ante el Consejo Regional de Mujeres de las Américas (CRA).</p>
                        <p>El CNMP no participa en actividades político partidarias, respeta las ideas políticas y las creencias religiosas de sus asociadas, así como la independencia y autonomía institucional de las asociaciones afiliadas que lo integran. Su duración es indefinida y su domicilio es la ciudad de Lima.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="section section--crema" id="fines">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Estatuto · Artículo 8</span>
                    <h2>Nuestros fines</h2>
                    <p class="lead">Ocho fines que orientan toda la acción del Consejo.</p>
                </div>
                <div class="aims">
                    {aims_html(FINES)}
                </div>
            </div>
        </section>

        <section class="section" id="historia">
            <div class="container">
                <div class="split">
                    <div class="split__media split__media--wide reveal">
                        <img src="img/historia/plaza-mayor-1907.jpg" alt="Plaza Mayor de Lima en 1907" loading="lazy">
                        <div class="split__badge">
                            <strong>1923</strong>
                            <span>Lima, 3 de marzo. Nace el Consejo Nacional de Mujeres del Perú</span>
                        </div>
                    </div>
                    <div class="split__content reveal reveal-delay-1">
                        <span class="eyebrow">Nuestra historia</span>
                        <h2>Un consejo para unir a las mujeres del Perú</h2>
                        <p>A inicios del siglo XX, Lima vivía el despertar del movimiento femenino. En 1914 María Jesús Alvarado Rivera había fundado Evolución Femenina, la primera organización feminista del país, y desde entonces surgieron nuevas asociaciones de mujeres dedicadas a la educación, la cultura y la beneficencia.</p>
                        <p>En 1923, la visita a Lima de Carrie Chapman Catt, presidenta de la Alianza Internacional por el Sufragio de la Mujer, fue la ocasión para dar un paso decisivo: el 3 de marzo de ese año se constituyó el Consejo Nacional de Mujeres del Perú como institución que federaba a las organizaciones femeninas existentes, a imagen de los consejos nacionales que integran el Consejo Internacional de Mujeres.</p>
                        <p>Entre sus primeras tareas estuvo la lucha por el reconocimiento de los derechos civiles y políticos de la mujer, en especial el derecho al voto, que el Perú reconocería recién en 1955. En 1926 el Consejo se afilió formalmente al Consejo Internacional de Mujeres, vínculo que mantiene hasta hoy.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="section section--azul">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Línea de tiempo</span>
                    <h2>Hitos de más de un siglo</h2>
                </div>
                <div class="timeline">
                    {timeline_html(TIMELINE)}
                </div>
            </div>
        </section>

        <section class="section" id="plaza-del-rosario">
            <div class="container">
                <div class="split split--reverse">
                    <div class="split__media reveal">
                        <img src="img/fotos/plaza-del-rosario.jpg" alt="Escultura de la Virgen del Rosario en la Plaza del Rosario, Jesús María" loading="lazy">
                        <div class="split__badge">
                            <strong>1988</strong>
                            <span>Bendecida por San Juan Pablo II el 14 de mayo</span>
                        </div>
                    </div>
                    <div class="split__content reveal reveal-delay-1">
                        <span class="eyebrow">Obra emblemática</span>
                        <h2>La Plaza del Rosario</h2>
                        <p>Se encuentra en el distrito de Jesús María, en la berma central de la sexta cuadra de la avenida Salaverry. Con quince metros de diámetro, representa el Rosario en alto relieve elaborado en bronce, con los misterios, las letanías y la oración del Magníficat.</p>
                        <p>Este proyecto mariano en homenaje a la Santísima Virgen del Rosario fue realizado para la segunda visita de S.S. Juan Pablo II, con motivo del Congreso Eucarístico Mariano de los Países Bolivarianos de mayo de 1988. Fue donado por su autor, el arquitecto César Díaz Gonzáles, y la escultura de la Virgen, en bronce y de tamaño natural, por el escultor Martín Salazar. El Consejo Nacional de Mujeres del Perú estuvo a cargo del proyecto, con el apoyo del Episcopado y la Nunciatura Apostólica, la empresa privada y la Municipalidad de Jesús María.</p>
                        <p>Para financiar la obra se difundió por la prensa una campaña de donación de bronce: el público respondió con generosidad y se reunieron seis toneladas aportadas por 1 080 personas, cuyos nombres ornamentan la parte externa de la plaza. El 12 de mayo se colocó la Virgen sobre su base de granito; el 13 de mayo el cardenal Ángel Suquía inauguró la plaza y el 14 de mayo S.S. Juan Pablo II impartió su bendición.</p>
                        <div class="quote-box">Desde 1988, por iniciativa del entonces nuncio apostólico, monseñor Luigi Dossena, el Movimiento Católico Plaza del Rosario convoca a personas de toda edad al rezo del Rosario los primeros sábados de cada mes a las 5:00 p.m., de manera ininterrumpida.</div>
                    </div>
                </div>
            </div>
        </section>

        <section class="section section--crema" id="pioneras">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Pioneras</span>
                    <h2>Las mujeres que forjaron el Consejo</h2>
                    <p class="lead">Educadoras, escritoras e intelectuales que abrieron camino a las peruanas de hoy.</p>
                </div>
                <div class="people">
{pioneras_html(PIONERAS)}                </div>
            </div>
        </section>

        <section class="section section--azul" id="emblemas">
            <div class="container">
                <div class="emblem">
                    <div class="emblem__logo reveal"><img src="img/logo-512.png" alt="Escudo del Consejo Nacional de Mujeres del Perú"></div>
                    <div class="reveal reveal-delay-1">
                        <span class="eyebrow">Estatuto · Artículo 85</span>
                        <h2>Nuestros emblemas</h2>
                        <p class="lead">El escudo del CNMP simboliza los supremos ideales de Dios, Patria y Sociedad.</p>
                        <ul class="emblem__list">
                            <li><i class="fas fa-flag"></i><div><strong>Estandarte Nacional</strong>con la inscripción «Consejo Nacional de Mujeres del Perú · 1923».</div></li>
                            <li><i class="fas fa-flag"></i><div><strong>Bandera de la institución</strong></div></li>
                            <li><i class="fas fa-shield-halved"></i><div><strong>Escudo del CNMP</strong>que simboliza los supremos ideales de Dios – Patria – Sociedad.</div></li>
                            <li><i class="fas fa-music"></i><div><strong>Himno de la institución</strong></div></li>
                            <li><i class="fas fa-medal"></i><div><strong>Insignia de metal y esmalte</strong>fondo blanco, cruz azul y escudo con los colores patrios al centro, rodeados de una corona de encina.</div></li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <section class="section" id="organizacion">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Estructura orgánica</span>
                    <h2>Cómo nos organizamos</h2>
                    <p class="lead">Cuatro órganos definidos por el estatuto, con comisiones permanentes de trabajo, filiales regionales y asociaciones afiliadas.</p>
                </div>
                <div class="grid grid--4">
                    <article class="card reveal">
                        <div class="card__icon"><i class="fas fa-users"></i></div>
                        <h3>Asamblea General</h3>
                        <p>Órgano de gobierno y máxima instancia. La integran las asociadas y las delegadas de las filiales y asociaciones afiliadas. Sesiona en forma ordinaria en marzo y noviembre.</p>
                    </article>
                    <article class="card reveal reveal-delay-1">
                        <div class="card__icon"><i class="fas fa-user-tie"></i></div>
                        <h3>Consejo Directivo</h3>
                        <p>Órgano de dirección y ejecutivo, elegido cada dos años por voto secreto y por listas. Lo integran la presidenta, dos vicepresidentas, secretarias, tesoreras y cuatro vocales.</p>
                    </article>
                    <article class="card reveal reveal-delay-2">
                        <div class="card__icon"><i class="fas fa-comments"></i></div>
                        <h3>Consejo Consultivo</h3>
                        <p>Órgano de asesoramiento, constituido por las past presidentas del CNMP, consideradas asociadas honorarias. Vela por el cumplimiento de los fines y propone candidatas a la Medalla del Consejo.</p>
                    </article>
                    <article class="card reveal reveal-delay-3">
                        <div class="card__icon"><i class="fas fa-check-to-slot"></i></div>
                        <h3>Comité Electoral</h3>
                        <p>Órgano electoral autónomo de cinco miembros, elegido por la Asamblea General Extraordinaria, que organiza y conduce cada proceso electoral.</p>
                    </article>
                </div>
                <div class="grid grid--3 mt-32">
                    <article class="card reveal">
                        <div class="card__icon"><i class="fas fa-diagram-project"></i></div>
                        <h3>Comisiones permanentes</h3>
                        <p>Nueve comisiones de trabajo que estudian, investigan y ejecutan las actividades vinculadas a los fines del Consejo. <a href="que-hacemos.html#comisiones">Ver las comisiones</a>.</p>
                    </article>
                    <article class="card reveal reveal-delay-1">
                        <div class="card__icon"><i class="fas fa-map-location-dot"></i></div>
                        <h3>Filiales regionales</h3>
                        <p>El CNMP puede establecer filiales en todas las regiones del país, con voz y voto en la Asamblea General a través de sus delegadas.</p>
                    </article>
                    <article class="card reveal reveal-delay-2">
                        <div class="card__icon"><i class="fas fa-people-group"></i></div>
                        <h3>Asociaciones afiliadas</h3>
                        <p>Organizaciones incorporadas al CNMP que conservan su autonomía y participan en las decisiones de la Asamblea General mediante sus delegadas.</p>
                    </article>
                </div>
            </div>
        </section>

        <section class="section section--crema" id="consejo-directivo">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Periodo 2025–2027</span>
                    <h2>Consejo Directivo</h2>
                    <p class="lead">Elegido conforme al estatuto y juramentado en ceremonia solemne en 2026.</p>
                </div>
                <div class="board">
                    <div class="board__photo reveal">
                        <img src="img/fotos/juramentacion-2026.jpg" alt="Integrantes del Consejo Directivo 2025–2027 durante la ceremonia de juramentación" loading="lazy">
                        <p class="board__caption">Ceremonia de juramentación del Consejo Directivo del CNMP para el periodo 2025–2027.</p>
                    </div>
                    <ul class="board__list reveal reveal-delay-1">
                        {board_html()}
                    </ul>
                </div>
            </div>
        </section>

        <section class="section" id="distinciones">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Estatuto · Artículo 74</span>
                    <h2>Distinciones que otorga el Consejo</h2>
                </div>
                <div class="grid grid--3">
                    <article class="card reveal"><div class="card__icon"><i class="fas fa-medal"></i></div><h3>Medalla de la Orden del Consejo</h3><p>Para quienes han destacado en actos cívicos al servicio de la comunidad o de la nación, en la investigación, en obras de bienestar social o en una labor institucional o profesional sobresaliente.</p></article>
                    <article class="card reveal reveal-delay-1"><div class="card__icon"><i class="fas fa-certificate"></i></div><h3>Diploma de honor</h3><p>Para peruanos, extranjeros e instituciones que hayan prestado servicios destacados en bien del CNMP, del país o de la comunidad.</p></article>
                    <article class="card reveal reveal-delay-2"><div class="card__icon"><i class="fas fa-award"></i></div><h3>Medalla de Asociada Honoraria</h3><p>Para las integrantes del Consejo Consultivo, past presidentas de la institución.</p></article>
                </div>
            </div>
        </section>

''' + cta())

# ================================================================ QUÉ HACEMOS
pages["que-hacemos.html"] = dict(
    title="Qué hacemos | Consejo Nacional de Mujeres del Perú",
    desc="Líneas de acción, objetivos y comisiones permanentes de trabajo del Consejo Nacional de Mujeres del Perú: derechos e igualdad, formación, familia y comunidad, conciliación y servicios.",
    path="que-hacemos.html",
    body=page_hero("Qué hacemos", "Los fines y objetivos de nuestro estatuto se traducen en líneas de acción concretas y en el trabajo de nueve comisiones permanentes.", "img/fotos/que-hacemos-hero.jpg", "Qué hacemos") + f'''
        <section class="section">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Líneas de acción</span>
                    <h2>Así trabajamos por la mujer peruana</h2>
                </div>

                <article class="program reveal" id="derechos">
                    <div class="program__media"><img src="img/fotos/programa-derechos.jpg" alt="Derechos e igualdad" loading="lazy"></div>
                    <div class="program__content">
                        <div class="program__num">01 · Derechos e igualdad</div>
                        <h3>Una voz por los derechos de la persona</h3>
                        <p>Promovemos el reconocimiento y el respeto de los derechos de la persona, la eliminación de toda forma de discriminación por razón de nacimiento, sexo, raza, idioma o religión, y la igualdad de derechos y responsabilidades entre el hombre y la mujer. Unimos esfuerzos para desterrar toda forma de violencia contra la mujer y el menor.</p>
                        <div class="program__tags"><span>Legislación y derechos humanos</span><span>Igualdad de oportunidades</span><span>Prevención de la violencia</span><span>Pronunciamientos</span></div>
                    </div>
                </article>

                <article class="program reveal" id="formacion">
                    <div class="program__media"><img src="img/fotos/programa-formacion.jpg" alt="Formación y participación" loading="lazy"></div>
                    <div class="program__content">
                        <div class="program__num">02 · Formación y participación</div>
                        <h3>Mujeres preparadas para la vida pública</h3>
                        <p>Fomentamos en las mujeres del Perú la toma de conciencia de sus responsabilidades en la familia y la sociedad, y las preparamos e incentivamos a participar en la vida pública del país mediante congresos, seminarios, foros y mesas redondas, en coordinación con filiales, asociaciones afiliadas, universidades e instituciones afines.</p>
                        <div class="program__tags"><span>Congresos y seminarios</span><span>Educación y profesiones</span><span>Ética y valores</span><span>Publicaciones y boletín</span></div>
                    </div>
                </article>

                <article class="program reveal" id="familia">
                    <div class="program__media"><img src="img/fotos/programa-familia.jpg" alt="Familia, salud y comunidad" loading="lazy"></div>
                    <div class="program__content">
                        <div class="program__num">03 · Familia, salud y comunidad</div>
                        <h3>Bienestar para la mujer y su familia</h3>
                        <p>A través de las comisiones de salud integral, bienestar social y proyección a la comunidad, y de desarrollo de la persona, el menor, la mujer, la familia y el adulto mayor, impulsamos acciones solidarias y de promoción humana, incluidos botiquines médicos y campañas de salud y bienestar.</p>
                        <div class="program__tags"><span>Salud integral</span><span>Proyección a la comunidad</span><span>Familia y adulto mayor</span><span>Campañas solidarias</span></div>
                    </div>
                </article>

                <article class="program reveal" id="conciliacion">
                    <div class="program__media"><img src="img/fotos/programa-cultura.jpg" alt="Conciliación, cultura y servicios" loading="lazy"></div>
                    <div class="program__content">
                        <div class="program__num">04 · Conciliación, cultura y servicios</div>
                        <h3>Soluciones y oportunidades</h3>
                        <p>El estatuto nos faculta a ejercer función conciliadora y otros medios alternativos de solución de conflictos, constituir centros de conciliación y capacitación extrajudicial, de educación y aprendizaje, y consultorios jurídicos; promover la constitución de microempresas; y elevar el nivel cultural de las personas mediante las comisiones de cultura, turismo, artesanía, folklore y ecología.</p>
                        <div class="program__tags"><span>Conciliación extrajudicial</span><span>Consultorios jurídicos</span><span>Microempresas</span><span>Cultura, turismo y ecología</span></div>
                    </div>
                </article>
            </div>
        </section>

        <section class="section section--azul" id="objetivos">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Estatuto · Artículo 9</span>
                    <h2>Nuestros objetivos</h2>
                </div>
                <div class="grid grid--3">
''' + "".join(f'''                    <article class="card reveal"><div class="card__icon"><i class="fas {ic}"></i></div><h3>{h}</h3><p>{p}</p></article>
''' for ic, h, p in OBJETIVOS) + f'''                </div>
            </div>
        </section>

        <section class="section section--crema" id="comisiones">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Estatuto · Artículo 65</span>
                    <h2>Comisiones permanentes de trabajo</h2>
                    <p class="lead">Cada comisión está integrada por asociadas inscritas según sus inquietudes y especialidades, con una coordinadora designada por la presidenta. Estudian, investigan y ejecutan las actividades de su área.</p>
                </div>
                <div class="commissions">
''' + "".join(f'                    <div class="commission reveal"><i class="fas {ic}"></i><span>{n}</span></div>\n' for ic, n in COMISIONES) + '''                </div>
            </div>
        </section>

        <section class="section" id="internacional">
            <div class="container">
                <div class="split">
                    <div class="split__media split__media--wide reveal">
                        <img src="img/fotos/participa-hero.jpg" alt="Plaza San Martín, Lima" loading="lazy">
                        <div class="split__badge"><strong>CIDEM · CRA</strong><span>Representación de la mujer peruana en el mundo</span></div>
                    </div>
                    <div class="split__content reveal reveal-delay-1">
                        <span class="eyebrow">Representación internacional</span>
                        <h2>La voz de la mujer peruana ante el mundo</h2>
                        <p>Desde 1926 el CNMP es la única institución que representa a la mujer peruana ante el Consejo Internacional de Mujeres (CIDEM), con sede en París, y ante el Consejo Regional de Mujeres de las Américas (CRA). El Consejo Directivo mantiene relación permanente con ambos organismos y con instituciones afines en el extranjero.</p>
                        <p>Llevamos la representación de la mujer peruana a los certámenes nacionales e internacionales donde se debaten asuntos relacionados con nuestros fines, y la presidenta rinde cuenta de su gestión ante el CIDEM y el CRA al término de cada mandato.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="cta cta--rojo">
            <div class="container">
                <div>
                    <h2>¿Quieres proponer o apoyar una actividad?</h2>
                    <p>Trabajamos con universidades, instituciones públicas y privadas y organizaciones que comparten nuestros fines.</p>
                </div>
                <div class="cta__actions">
                    <a class="btn btn--white" href="contacto.html?asunto=alianza">Conversemos</a>
                </div>
            </div>
        </section>
''')

# ================================================================ PARTICIPA
pages["participa.html"] = dict(
    title="Participa | Consejo Nacional de Mujeres del Perú",
    desc="Afíliate al Consejo Nacional de Mujeres del Perú como asociada, integra a tu asociación o constituye una filial regional. Derechos, deberes y proceso de admisión según el estatuto.",
    path="participa.html",
    body=page_hero("Participa", "Ciudadanas, asociaciones y filiales regionales integran el Consejo. Conoce cómo sumarte a más de un siglo de trabajo por la mujer peruana.", "img/fotos/participa-hero.jpg", "Participa") + '''
        <section class="section">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Estatuto · Artículo 52</span>
                    <h2>Quiénes integran el Consejo</h2>
                    <p class="lead">El CNMP está conformado por asociadas activas y honorarias, por sus filiales regionales y por las asociaciones afiliadas.</p>
                </div>
                <div class="ways">
                    <div class="way reveal" id="afiliacion">
                        <div class="way__icon"><i class="fas fa-id-card"></i></div>
                        <h3>Asociadas</h3>
                        <p>Ciudadanas que se identifican con los fines del Consejo y participan activamente en sus comisiones y actividades.</p>
                        <ul>
                            <li>Voz y voto en las asambleas generales</li>
                            <li>Elegir y ser elegida para cargos directivos</li>
                            <li>Presentar proyectos al Consejo Directivo</li>
                            <li>Carné, insignia, diploma de miembro y estatuto</li>
                        </ul>
                        <a class="btn btn--primary" href="contacto.html?asunto=afiliacion">Quiero afiliarme</a>
                    </div>
                    <div class="way reveal reveal-delay-1" id="asociaciones">
                        <div class="way__icon"><i class="fas fa-people-group"></i></div>
                        <h3>Asociaciones afiliadas</h3>
                        <p>Organizaciones incorporadas al CNMP que conservan su independencia y autonomía institucional.</p>
                        <ul>
                            <li>Voz y voto en las asambleas a través de sus delegadas</li>
                            <li>Apoyo para planificar programas, proyectos e investigaciones</li>
                            <li>Proponer candidatos a la Medalla de la Orden del Consejo</li>
                            <li>Constancia de afiliación, estatuto y reglamento</li>
                        </ul>
                        <a class="btn btn--azul" href="contacto.html?asunto=asociacion">Afiliar mi asociación</a>
                    </div>
                    <div class="way reveal reveal-delay-2" id="filiales">
                        <div class="way__icon"><i class="fas fa-map-location-dot"></i></div>
                        <h3>Filiales regionales</h3>
                        <p>El Consejo puede constituir filiales en todas las regiones del país, denominadas «CNMP filial» seguido del nombre que corresponda.</p>
                        <ul>
                            <li>Voz y voto a través de sus delegadas</li>
                            <li>Coordinación permanente con el CNMP</li>
                            <li>Participación en los planes nacionales</li>
                            <li>Apoyo para programas y proyectos regionales</li>
                        </ul>
                        <a class="btn btn--outline" href="contacto.html?asunto=filial">Constituir una filial</a>
                    </div>
                </div>
            </div>
        </section>

        <section class="section section--crema">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Admisión</span>
                    <h2>Cómo afiliarte en cuatro pasos</h2>
                </div>
                <div class="steps">
                    <div class="step reveal"><h4>Escríbenos</h4><p>Completa el formulario de contacto o escríbenos por correo o WhatsApp indicando tu interés en afiliarte o en afiliar a tu asociación.</p></div>
                    <div class="step reveal reveal-delay-1"><h4>Solicitud</h4><p>La Secretaría General recibe tu solicitud de incorporación y la remite al Comité Calificador de Admisión, presidido por la primera vicepresidenta.</p></div>
                    <div class="step reveal reveal-delay-2"><h4>Evaluación</h4><p>El Comité Calificador evalúa la solicitud y la propone al Consejo Directivo conforme al estatuto y al reglamento.</p></div>
                    <div class="step reveal reveal-delay-3"><h4>Incorporación</h4><p>Recibes tu carné de asociada, la insignia, el diploma de miembro y el estatuto, y te integras a una comisión permanente de trabajo.</p></div>
                </div>
            </div>
        </section>

        <section class="section" id="deberes">
            <div class="container">
                <div class="split">
                    <div class="split__content reveal">
                        <span class="eyebrow">Estatuto · Artículo 54</span>
                        <h2>Deberes de las asociadas</h2>
                        <p>Ser asociada del Consejo es también un compromiso con la institución y con sus fines.</p>
                        <ul class="checklist">
                            <li><i class="fas fa-circle-check"></i><span>Cumplir con el estatuto y los acuerdos de las asambleas generales.</span></li>
                            <li><i class="fas fa-circle-check"></i><span>Observar una conducta ética y respetable.</span></li>
                            <li><i class="fas fa-circle-check"></i><span>Difundir los fines y objetivos del CNMP.</span></li>
                            <li><i class="fas fa-circle-check"></i><span>Asistir a las asambleas generales y desempeñar las funciones que se le encomienden.</span></li>
                            <li><i class="fas fa-circle-check"></i><span>Cumplir con el pago oportuno de las cuotas.</span></li>
                            <li><i class="fas fa-circle-check"></i><span>Integrar comisiones de trabajo y comisiones especiales cuando se requiera.</span></li>
                        </ul>
                    </div>
                    <div class="split__media reveal reveal-delay-1">
                        <img src="img/fotos/sede-lima.jpg" alt="Plaza Mayor de Lima" loading="lazy">
                    </div>
                </div>
            </div>
        </section>

        <section class="section section--crema" id="preguntas">
            <div class="container">
                <div class="section__header reveal">
                    <span class="eyebrow">Preguntas frecuentes</span>
                    <h2>Resolvemos tus dudas</h2>
                </div>
                <div class="faq reveal">
                    <div class="faq__item">
                        <button class="faq__q" aria-expanded="false">¿Quiénes pueden afiliarse al Consejo?<i class="fas fa-plus"></i></button>
                        <div class="faq__a"><p>Ciudadanas que se identifican con los fines del CNMP y desean participar activamente en sus actividades, así como asociaciones y organizaciones de mujeres que compartan esos fines. La admisión la evalúa el Comité Calificador de Admisión y la aprueba el Consejo Directivo.</p></div>
                    </div>
                    <div class="faq__item">
                        <button class="faq__q" aria-expanded="false">¿Tiene costo ser asociada?<i class="fas fa-plus"></i></button>
                        <div class="faq__a"><p>Sí. El Consejo se sostiene con las cuotas ordinarias y extraordinarias de sus asociadas, además de donaciones y legados. El monto de las cuotas lo propone el Consejo Directivo y lo aprueba la Asamblea General; se informa durante el proceso de incorporación.</p></div>
                    </div>
                    <div class="faq__item">
                        <button class="faq__q" aria-expanded="false">¿Puedo participar si vivo fuera de Lima?<i class="fas fa-plus"></i></button>
                        <div class="faq__a"><p>Sí. El CNMP es de carácter nacional, puede establecer filiales en todas las regiones del país y celebrar reuniones en cualquier sede filial. Las filiales participan en la Asamblea General a través de sus delegadas.</p></div>
                    </div>
                    <div class="faq__item">
                        <button class="faq__q" aria-expanded="false">¿El Consejo tiene vinculación política o religiosa?<i class="fas fa-plus"></i></button>
                        <div class="faq__a"><p>No. Conforme a su estatuto, el CNMP no participa en actividades político partidarias y respeta las ideas políticas y las creencias religiosas de sus asociadas.</p></div>
                    </div>
                    <div class="faq__item">
                        <button class="faq__q" aria-expanded="false">¿Cómo se elige al Consejo Directivo?<i class="fas fa-plus"></i></button>
                        <div class="faq__a"><p>Cada dos años, en la segunda quincena de febrero, mediante votación secreta por el sistema de listas, conducida por un Comité Electoral autónomo elegido en Asamblea General Extraordinaria. Tienen derecho a voto las asociadas que figuran en el padrón de asociadas hábiles.</p></div>
                    </div>
                    <div class="faq__item">
                        <button class="faq__q" aria-expanded="false">¿Cómo puede apoyar mi empresa u organización?<i class="fas fa-plus"></i></button>
                        <div class="faq__a"><p>El Consejo puede celebrar acuerdos, convenios y contratos, y aceptar donaciones y legados de personas naturales o jurídicas, públicas o privadas, nacionales o internacionales, conforme a sus fines y objetivos. Escríbenos y diseñemos juntos una alianza.</p></div>
                    </div>
                </div>
            </div>
        </section>

        <section class="cta cta--rojo">
            <div class="container">
                <div>
                    <h2>Da el primer paso hoy</h2>
                    <p>Escríbenos y conversemos sobre cómo puedes ser parte del Consejo Nacional de Mujeres del Perú.</p>
                </div>
                <div class="cta__actions">
                    <a class="btn btn--white" href="contacto.html">Ir al formulario de contacto</a>
                </div>
            </div>
        </section>
''')

# ================================================================ CONTACTO
pages["contacto.html"] = dict(
    title="Contacto | Consejo Nacional de Mujeres del Perú",
    desc="Contacta al Consejo Nacional de Mujeres del Perú: afiliación de asociadas y asociaciones, filiales, alianzas institucionales y consultas generales.",
    path="contacto.html",
    body=page_hero("Contacto", "Nuestro domicilio institucional está en Lima y atendemos consultas de todo el Perú. Escríbenos y te responderemos a la brevedad.", "img/fotos/contacto-hero.jpg", "Contacto") + f'''
        <section class="section">
            <div class="container">
                <div class="contact">
                    <div class="reveal">
                        <span class="eyebrow">Conversemos</span>
                        <h2>Estamos para escucharte</h2>
                        <p class="lead" style="margin-bottom:28px">Si deseas afiliarte, integrar a tu asociación, proponer una alianza o conocer más sobre nuestro trabajo, estos son nuestros canales.</p>
                        <div class="contact__info">
                            <div class="contact__item"><i class="fas fa-phone"></i><div><h4>Teléfono / WhatsApp</h4><a href="tel:{TEL_LINK}">{TEL}</a></div></div>
                            <div class="contact__item"><i class="fas fa-envelope"></i><div><h4>Correo electrónico</h4><a href="mailto:{MAIL}">{MAIL}</a></div></div>
                            <div class="contact__item"><i class="fab fa-facebook-f"></i><div><h4>Facebook</h4><a href="{FB}" target="_blank" rel="noopener noreferrer">Consejo Nacional de Mujeres del Perú</a></div></div>
                            <div class="contact__item"><i class="fas fa-location-dot"></i><div><h4>Sede</h4><p>Lima, Perú. Atención previa coordinación.</p></div></div>
                        </div>
                    </div>
                    <form class="form reveal reveal-delay-1" action="contacto.php" method="post" data-ajax novalidate>
                        <div class="form__row">
                            <div class="form__group"><label for="nombre">Nombre y apellidos *</label><input type="text" id="nombre" name="nombre" required autocomplete="name" placeholder="Tu nombre completo"></div>
                            <div class="form__group"><label for="email">Correo electrónico *</label><input type="email" id="email" name="email" required autocomplete="email" placeholder="nombre@correo.com"></div>
                        </div>
                        <div class="form__row">
                            <div class="form__group"><label for="telefono">Teléfono</label><input type="tel" id="telefono" name="telefono" autocomplete="tel" placeholder="+51 999 999 999"></div>
                            <div class="form__group"><label for="asunto">Motivo *</label>
                                <select id="asunto" name="asunto" required>
                                    <option value="">Selecciona una opción</option>
                                    <option value="afiliacion">Quiero afiliarme como asociada</option>
                                    <option value="asociacion">Afiliación de una asociación</option>
                                    <option value="filial">Constitución de una filial regional</option>
                                    <option value="voluntariado">Quiero colaborar en una comisión</option>
                                    <option value="alianza">Propuesta de alianza o convenio</option>
                                    <option value="prensa">Prensa y comunicaciones</option>
                                    <option value="consulta">Consulta general</option>
                                </select>
                            </div>
                        </div>
                        <div class="form__group"><label for="mensaje">Mensaje *</label><textarea id="mensaje" name="mensaje" required placeholder="Cuéntanos en qué podemos ayudarte"></textarea></div>
                        <div class="hp" aria-hidden="true"><label>No completar<input type="text" name="sitio_web" tabindex="-1" autocomplete="off"></label></div>
                        <div class="form__group"><label class="form__check"><input type="checkbox" name="privacidad" value="1" required><span>Autorizo el tratamiento de mis datos personales para atender esta consulta, conforme a la Ley N.° 29733 de Protección de Datos Personales.</span></label></div>
                        <button class="btn btn--primary" type="submit"><i class="fas fa-paper-plane"></i> Enviar mensaje</button>
                        <div class="form__status" role="status" aria-live="polite"></div>
                    </form>
                </div>
            </div>
        </section>
''')

# ================================================================ CRÉDITOS
CREDITOS = [
    ("Ceremonia de juramentación del Consejo Directivo 2025–2027", "Archivo del Consejo Nacional de Mujeres del Perú", "Derechos reservados", None),
    ("Plaza del Rosario, Jesús María", "Archivo del Consejo Nacional de Mujeres del Perú", "Derechos reservados", None),
    ("Bodas de Plata del Doctorado en Economía (UNFV)", "Universidad Nacional Federico Villarreal, nota de prensa", "Cortesía UNFV", "https://www.unfv.edu.pe/noticias/primera-promocion-del-doctorado-en-economia-celebro-25-anos-de-culminacion-de-sus-estudios"),
    ("Panorámica de la Plaza Mayor de Lima (portada)", "F Delventhal", "CC BY 2.0", "https://commons.wikimedia.org/wiki/File:Plaza_Mayor_Lima_pano.jpg"),
    ("Plaza Mayor de Lima, 1907", "C. Reginald Enock, «The Andes and the Amazon» (1907)", "Dominio público", "https://commons.wikimedia.org/wiki/File:Plaza_Mayor_de_Lima,_1907.jpg"),
    ("La Plaza Mayor, Lima", "YusmarBlanco", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:La_Plaza_Mayor,_Lima,_Peru.jpg"),
    ("Gran Biblioteca Pública de Lima", "Kbu2024", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Gran_Biblioteca_P%C3%BAblica_de_Lima_01.jpg"),
    ("Plaza San Martín, Lima (vista general)", "David Berkowitz", "CC BY 2.0", "https://commons.wikimedia.org/wiki/File:San_Martin_Plaza,_Lima-1.jpg"),
    ("Plaza San Martín, Lima", "Ministerio de Defensa del Perú", "CC BY 2.0", "https://commons.wikimedia.org/wiki/File:Plaza_San_Mart%C3%ADn,_Lima_Peru.jpg"),
    ("Malecón de Miraflores, Lima", "Alec Gamoff", "CC BY 2.0", "https://commons.wikimedia.org/wiki/File:Malec%C3%B3n_de_Miraflores,_Lima.jpg"),
    ("Casona de San Marcos", "Ovruni", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Casona_de_San_Marcos.jpg"),
    ("Parque Kennedy, Miraflores", "Francisco Anzola", "CC BY 2.0", "https://commons.wikimedia.org/wiki/File:Parque_Kennedy_Miraflores_(3912337253).jpg"),
    ("Teatro Municipal de Lima", "Diego Delso, delso.photo", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Teatro_municipal,_Lima,_Per%C3%BA,_2015-07-28,_DD_10.JPG"),
    ("Palacio Legislativo del Perú", "Herwarth Morales", "CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:Palacio_del_congreso_de_la_Rep%C3%BAblica_del_Per%C3%BA.jpg"),
    ("Retrato de María Jesús Alvarado Rivera", "University of Florida Digital Collections", "Dominio público", "https://commons.wikimedia.org/wiki/File:Mar%C3%ADa_Jes%C3%BAs_Alvarado_Rivera_(cropped).png"),
    ("Retrato de Mercedes Gallagher de Parks (1928)", "Courret Hermanos, Biblioteca Nacional del Perú", "Dominio público", "https://commons.wikimedia.org/wiki/File:Mercedes_Alicia_Gallagher_Ortiz_de_Villate.jpg"),
    ("Retrato de Elvira García y García", "Archivo fotográfico de la Biblioteca Nacional del Perú", "Dominio público", "https://commons.wikimedia.org/wiki/File:Elvira_Garc%C3%ADa_y_Garc%C3%ADa.jpg"),
    ("Retrato de Angélica Palma", "Bernardo Uribe Muñoz, «Mujeres de América» (1935)", "Dominio público", "https://commons.wikimedia.org/wiki/File:Mar%C3%ADa_Ang%C3%A9lica_Palma_y_Rom%C3%A1n.png"),
    ("Retrato de Carrie Chapman Catt", "Theodore C. Marceau, National Portrait Gallery", "Dominio público", "https://commons.wikimedia.org/wiki/File:Carrie_Chapman_Catt_NPG.jpg"),
]
rows = "".join(f'<tr><td>{t}</td><td>{a}</td><td>{l}</td><td>{("<a href=%s target=_blank rel=noopener>Ver fuente</a>" % repr(u)) if u else "—"}</td></tr>' for t, a, l, u in CREDITOS)
pages["creditos.html"] = dict(
    title="Créditos fotográficos | Consejo Nacional de Mujeres del Perú",
    desc="Autoría y licencias de las fotografías utilizadas en el sitio web del Consejo Nacional de Mujeres del Perú.",
    path="creditos.html",
    body='''        <section class="section">
            <div class="container">
                <div class="section__header section__header--left reveal">
                    <span class="eyebrow">Transparencia</span>
                    <h2>Créditos fotográficos</h2>
                    <p class="lead">Las fotografías institucionales pertenecen al archivo del Consejo. Las imágenes históricas y de Lima provienen de Wikimedia Commons y se utilizan bajo licencias Creative Commons o por encontrarse en dominio público. Agradecemos a sus autores.</p>
                </div>
                <div class="table-wrap reveal">
                    <table class="table">
                        <thead><tr><th>Imagen</th><th>Autor / fuente</th><th>Licencia</th><th>Enlace</th></tr></thead>
                        <tbody>''' + rows + '''</tbody>
                    </table>
                </div>
                <p class="mt-32">El escudo y los emblemas del Consejo Nacional de Mujeres del Perú son propiedad de la institución. Las licencias Creative Commons se detallan en <a href="https://creativecommons.org/licenses/" target="_blank" rel="noopener noreferrer">creativecommons.org</a>.</p>
            </div>
        </section>
''')

# ================================================================ 404
pages["404.html"] = dict(
    title="Página no encontrada | Consejo Nacional de Mujeres del Perú",
    desc="La página que buscas no existe o fue movida.",
    path="404.html",
    body='''        <section class="page-404 section">
            <div class="container">
                <h1>404</h1>
                <h2>Página no encontrada</h2>
                <p class="lead">La página que buscas no existe o fue movida. Te invitamos a volver al inicio.</p>
                <div class="btn-group mt-32" style="justify-content:center">
                    <a class="btn btn--primary" href="index.html">Volver al inicio</a>
                    <a class="btn btn--outline" href="contacto.html">Contáctanos</a>
                </div>
            </div>
        </section>
''')

for name, p in pages.items():
    html = head(p["title"], p["desc"], p["path"], SCHEMA if p.get("schema") else "") + header() + p["body"] + footer()
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name, len(html))

# historia.html ahora vive dentro de nosotros.html
with open(os.path.join(ROOT, "historia.html"), "w", encoding="utf-8") as f:
    f.write('''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Historia | Consejo Nacional de Mujeres del Perú</title>
    <meta http-equiv="refresh" content="0; url=nosotros.html#historia">
    <link rel="canonical" href="https://consejonacionaldemujeresdelperu.com/nosotros.html">
    <meta name="robots" content="noindex">
</head>
<body>
    <p>La historia del Consejo ahora está en <a href="nosotros.html#historia">Nosotros</a>.</p>
</body>
</html>
''')
print("wrote historia.html (redirección)")


# ================================================================ NOTICIAS
import unicodedata, datetime, json, re
from email.utils import format_datetime
def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")
def json_s(s): return json.dumps(s, ensure_ascii=False)
CATEGORIAS = {"institucional": "Institucional", "presidencia": "Presidencia", "historia": "Historia", "actividades": "Actividades"}
NOTICIAS = [
 dict(slug="juramentacion-consejo-directivo-2025-2027", cat="institucional", date="2026-11-12", date_text="2026",
      title="Juramentó el Consejo Directivo para el periodo 2025–2027",
      excerpt="En ceremonia solemne, las integrantes del nuevo Consejo Directivo, presidido por María Amelia Asenjo Azpilcueta, asumieron sus cargos conforme al estatuto.",
      image="img/fotos/juramentacion-2026.jpg", image_alt="Integrantes del Consejo Directivo 2025–2027 durante la ceremonia de juramentación", credit="Archivo del Consejo Nacional de Mujeres del Perú",
      tags=["Consejo Directivo", "Juramentación", "Estatuto"],
      body="""<p>Durante el presente año 2026 se realizó la ceremonia de juramentación del Consejo Directivo del Consejo Nacional de Mujeres del Perú (CNMP) para el periodo 2025–2027. Conforme al estatuto, el Consejo Directivo es el órgano ejecutivo de la institución: es elegido cada dos años por voto secreto y por el sistema de listas, es proclamado por la presidenta del Comité Electoral y asume sus cargos en acto solemne.</p>
<h2>Integrantes del Consejo Directivo 2025–2027</h2>
<ul class="post__list">""" + "".join(f"<li><strong>{r}:</strong> {n}</li>" for r, n in CONSEJO) + """</ul>
<p>El Consejo Directivo tiene entre sus atribuciones formular el plan de trabajo anual, aprobar los proyectos de las comisiones permanentes, mantener relación permanente con el Consejo Internacional de Mujeres (CIDEM) y el Consejo Regional de Mujeres de las Américas (CRA), y designar representantes ante organismos nacionales e internacionales.</p>
<p>La presidenta es la representante legal del CNMP en el país y en el extranjero, preside las sesiones del Consejo Directivo y las asambleas generales, y rinde cuenta de su gestión ante la Asamblea General, el CIDEM y el CRA al término de su mandato.</p>
<p><a href="../nosotros.html#consejo-directivo">Conoce al Consejo Directivo y la estructura orgánica del CNMP</a>.</p>"""),
 dict(slug="bodas-de-plata-doctorado-economia-unfv", cat="presidencia", date="2026-11-09", date_text="7 de noviembre de 2026",
      title="Nuestra presidenta celebró las Bodas de Plata de la primera promoción del Doctorado en Economía de la UNFV",
      excerpt="La Universidad Nacional Federico Villarreal rindió homenaje a la primera promoción del Doctorado en Economía «Amartya Sen», a 25 años de la culminación de sus estudios.",
      image="img/fotos/noticia-unfv-2026.jpg", image_alt="Ceremonia por las Bodas de Plata de la primera promoción del Doctorado en Economía de la UNFV", credit="Universidad Nacional Federico Villarreal",
      tags=["Presidencia", "UNFV", "Educación superior"],
      body="""<p>María Amelia Asenjo Azpilcueta, presidenta del Consejo Nacional de Mujeres del Perú, integra la primera promoción del Doctorado en Economía «Amartya Sen» de la Escuela Universitaria de Posgrado de la Universidad Nacional Federico Villarreal (UNFV), que el sábado 7 de noviembre de 2026 celebró sus Bodas de Plata: veinticinco años de la culminación de sus estudios doctorales.</p>
<p>La ceremonia, realizada en el auditorio de la Facultad de Ciencias Económicas, fue presidida por la rectora de la universidad, Dra. Cristina Asunción Alzamora Rivero, quien destacó la trayectoria profesional de las y los integrantes de la promoción y su vínculo permanente con la casa de estudios. Participaron también el vicerrector de Investigación, Dr. Pedro Manuel Amaya Pingo, y el decano de la Facultad de Ciencias Económicas, Dr. Joel Jurado Nájera.</p>
<p>La promoción lleva el nombre del economista indio Amartya Sen, Premio Nobel de Economía 1998, cuyo trabajo sobre desarrollo humano y capacidades ha inspirado a generaciones de profesionales. Durante la ceremonia se rindió homenaje a los integrantes fallecidos y se reconoció el aporte de la promoción al desarrollo del país.</p>
<p>Para el Consejo, la formación académica de sus asociadas es parte de su compromiso estatutario de promover la superación individual y colectiva de la persona y de preparar a las mujeres del Perú para participar en la vida pública del país.</p>
<p><a href="https://www.unfv.edu.pe/noticias/primera-promocion-del-doctorado-en-economia-celebro-25-anos-de-culminacion-de-sus-estudios" target="_blank" rel="noopener noreferrer">Leer la nota de prensa de la UNFV <i class="fas fa-arrow-up-right-from-square"></i></a></p>"""),
 dict(slug="plaza-del-rosario-historia", cat="historia", date="2026-11-12", date_text="Mayo de 1988",
      title="La Plaza del Rosario: la obra que el Consejo levantó en tiempo récord para la visita de Juan Pablo II",
      excerpt="Seis toneladas de bronce donadas por 1 080 personas, una escultura de la Virgen y una plaza inaugurada en Jesús María en mayo de 1988. Esta es su historia.",
      image="img/fotos/plaza-del-rosario.jpg", image_alt="Escultura de la Virgen del Rosario en la Plaza del Rosario, Jesús María", credit="Archivo del Consejo Nacional de Mujeres del Perú",
      tags=["Plaza del Rosario", "Jesús María", "Juan Pablo II", "Patrimonio"],
      body="""<p>La Plaza del Rosario se encuentra en el distrito de Jesús María, en la berma central de la sexta cuadra de la avenida Salaverry. Tiene quince metros de diámetro y representa el Rosario en alto relieve, elaborado en bronce, con los misterios, las letanías, la oración del Magníficat y más.</p>
<h2>Un proyecto mariano para la visita del Papa</h2>
<p>Este proyecto en homenaje a la Santísima Virgen del Rosario fue realizado para la segunda visita de S.S. Juan Pablo II al Perú, con motivo del Congreso Eucarístico Mariano de los Países Bolivarianos, en mayo de 1988. Fue donado por su autor, el arquitecto César Díaz Gonzáles. La escultura de la Virgen del Rosario, en bronce y de tamaño natural, fue donada por el escultor nacional Martín Salazar.</p>
<p>El Consejo Nacional de Mujeres del Perú, institución civil sin fines de lucro, estuvo a cargo del proyecto, con el apoyo del Episcopado y la Nunciatura Apostólica, la empresa privada y la Municipalidad de Jesús María.</p>
<h2>La campaña del bronce</h2>
<p>Para obtener los medios para su ejecución se recurrió a los medios de prensa, difundiendo la campaña de bronce que proporcionaría los recursos para realizar el proyecto. El público respondió generosamente: se reunieron seis toneladas donadas por 1 080 personas, cuyos nombres ornamentan la parte externa de la plaza. Con ese bronce se hicieron las cuentas del Rosario, la medalla, la cruz y la escultura de la Virgen. La plaza estuvo lista en tiempo récord.</p>
<blockquote>El 12 de mayo se colocó la Virgen del Rosario sobre una base de granito. El 13 de mayo, con el entusiasmo del Congreso Eucarístico Mariano y la presencia de ilustres visitantes, el cardenal Ángel Suquía inauguró la plaza, y el 14 de mayo S.S. Juan Pablo II impartió su bendición.</blockquote>
<h2>El Movimiento Católico Plaza del Rosario</h2>
<p>Luego se formó el Movimiento Católico Plaza del Rosario, a iniciativa del entonces nuncio apostólico, monseñor Luigi Dossena, como un recinto de oración y difusión del Santo Rosario, según el deseo del Santo Padre. Desde 1988, de manera ininterrumpida, invita a personas de toda edad y lugar a unirse al rezo del Rosario los primeros sábados de cada mes a las 5:00 p.m.</p>
<p><a href="rezo-del-rosario-primeros-sabados.html">Conoce la actividad mensual en la Plaza del Rosario</a>.</p>"""),
 dict(slug="rezo-del-rosario-primeros-sabados", cat="actividades", date="2026-11-12", date_text="Primeros sábados de cada mes",
      title="Rezo del Rosario en la Plaza del Rosario: primeros sábados de cada mes a las 5:00 p.m.",
      excerpt="Desde 1988, de manera ininterrumpida, el Movimiento Católico Plaza del Rosario convoca al rezo del Santo Rosario en la plaza que el Consejo levantó en Jesús María.",
      image="img/fotos/plaza-del-rosario.jpg", image_alt="Plaza del Rosario, avenida Salaverry, Jesús María", credit="Archivo del Consejo Nacional de Mujeres del Perú",
      tags=["Plaza del Rosario", "Actividad permanente", "Jesús María"],
      body="""<p>Todos los primeros sábados de cada mes, a las 5:00 p.m., el Movimiento Católico Plaza del Rosario convoca a personas de toda edad y lugar al rezo del Santo Rosario en la Plaza del Rosario, ubicada en la berma central de la sexta cuadra de la avenida Salaverry, en el distrito de Jesús María.</p>
<p>La actividad se realiza de manera ininterrumpida desde 1988, año en que la plaza fue inaugurada y bendecida por S.S. Juan Pablo II durante su segunda visita al Perú. El movimiento nació por iniciativa del entonces nuncio apostólico, monseñor Luigi Dossena, como un recinto de oración y de difusión del Santo Rosario.</p>
<h2>Datos de la actividad</h2>
<ul class="post__list">
<li><strong>Cuándo:</strong> primer sábado de cada mes, 5:00 p.m.</li>
<li><strong>Dónde:</strong> Plaza del Rosario, av. Salaverry cuadra 6, Jesús María, Lima.</li>
<li><strong>Quiénes:</strong> abierta a todo público.</li>
</ul>
<p>El Consejo Nacional de Mujeres del Perú tuvo a su cargo la construcción de la plaza en 1988. <a href="plaza-del-rosario-historia.html">Lee la historia completa de la Plaza del Rosario</a>.</p>"""),
 dict(slug="fundacion-del-consejo-3-de-marzo-de-1923", cat="historia", date="2026-11-12", date_text="3 de marzo de 1923",
      title="3 de marzo de 1923: así nació el Consejo Nacional de Mujeres del Perú",
      excerpt="La visita de Carrie Chapman Catt a Lima, el impulso de María Jesús Alvarado y una generación de educadoras y escritoras dieron origen a la institución que desde 1926 representa a la mujer peruana ante el Consejo Internacional de Mujeres.",
      image="img/historia/plaza-mayor-1907.jpg", image_alt="Plaza Mayor de Lima a inicios del siglo XX", credit="C. Reginald Enock, «The Andes and the Amazon» (1907), dominio público",
      tags=["Fundación", "1923", "María Jesús Alvarado", "CIDEM", "Voto femenino"],
      body="""<p>A inicios del siglo XX, Lima vivía el despertar del movimiento femenino. En 1914 María Jesús Alvarado Rivera había fundado Evolución Femenina, la primera organización feminista del país, y desde entonces surgieron nuevas asociaciones de mujeres dedicadas a la educación, la cultura y la beneficencia.</p>
<p>En 1923, la visita a Lima de Carrie Chapman Catt, presidenta de la Alianza Internacional por el Sufragio de la Mujer, fue la ocasión para dar un paso decisivo: el 3 de marzo de ese año se constituyó el Consejo Nacional de Mujeres del Perú como institución que federaba a las organizaciones femeninas existentes, a imagen de los consejos nacionales que integran el Consejo Internacional de Mujeres, fundado en 1888.</p>
<h2>Las primeras dirigentes</h2>
<p>María Jesús Alvarado asumió la secretaría y Mercedes Gallagher de Parks, escritora y crítica de arte, la presidencia del comité directivo. En las sesiones de 1925, celebradas en el Liceo Grau, participaban también Amalia Puga de Losada, Ester Festini de Ramos Ocampo, Luisa Dammert, Elvira García y García y Elvira Rodrigues Lorente. En diciembre de 1924 Lima fue sede de la Segunda Conferencia Panamericana de Mujeres, presidida por la presidenta del Consejo.</p>
<h2>La afiliación internacional</h2>
<p>En 1926 el Consejo se afilió al Consejo Internacional de Mujeres (CIDEM), con sede en París, manteniendo autonomía en su organización interna y en su actividad nacional. Desde entonces es la única institución que representa a la mujer peruana ante el CIDEM y ante el Consejo Regional de Mujeres de las Américas (CRA).</p>
<p>Entre sus primeras causas estuvo el reconocimiento de los derechos civiles y políticos de la mujer, en especial el derecho al voto, que el Perú reconocería recién en 1955 con la Ley 12391. En 1969 el Consejo reconoció a María Jesús Alvarado como «la primera adalid moderna de los derechos de la mujer en el Perú».</p>
<p><a href="../nosotros.html#historia">Recorre la línea de tiempo completa del Consejo</a>.</p>"""),
]
for n in NOTICIAS:
    n["url"] = f"noticias/{n['slug']}.html"
    n["words"] = len(re.sub(r"<[^>]+>", " ", n["body"]).split())
    n["minutes"] = max(1, round(n["words"] / 200))
    n["tag_slugs"] = [slugify(x) for x in n["tags"]]
    n["search"] = slugify(" ".join([n["title"], n["excerpt"], CATEGORIAS[n["cat"]]] + n["tags"])).replace("-", " ")
ALL_TAGS = {}
for n in NOTICIAS:
    for tg, sl in zip(n["tags"], n["tag_slugs"]):
        ALL_TAGS.setdefault(sl, [tg, 0]); ALL_TAGS[sl][1] += 1
CAT_COUNT = {c: sum(1 for n in NOTICIAS if n["cat"] == c) for c in CATEGORIAS}

def news_card(n, rel=""):
    tags = "".join(f'<a class="tag" href="{rel}noticias.html?etiqueta={s}">{tg}</a>' for tg, s in zip(n["tags"], n["tag_slugs"]))
    return f'''                    <article class="news-card reveal" data-category="{n['cat']}" data-tags="{','.join(n['tag_slugs'])}" data-search="{n['search']}">
                        <a class="news-card__img" href="{rel}{n['url']}"><img src="{rel}{n['image']}" alt="{n['image_alt']}" loading="lazy"><span class="news-card__cat">{CATEGORIAS[n['cat']]}</span></a>
                        <div class="news-card__body">
                            <span class="news-card__date"><i class="far fa-calendar"></i> {n['date_text']} &middot; {n['minutes']} min de lectura</span>
                            <h3><a href="{rel}{n['url']}">{n['title']}</a></h3>
                            <p>{n['excerpt']}</p>
                            <div class="tags">{tags}</div>
                            <a class="card__link" href="{rel}{n['url']}">Leer la nota <i class="fas fa-arrow-right"></i></a>
                        </div>
                    </article>
'''

cat_chips = '<button class="chip is-active" data-filter="todas">Todas <span>' + str(len(NOTICIAS)) + '</span></button>' + "".join(
    f'<button class="chip" data-filter="{c}">{CATEGORIAS[c]} <span>{CAT_COUNT[c]}</span></button>' for c in CATEGORIAS if CAT_COUNT[c])
tag_cloud = "".join(f'<button class="tag" data-tag="{s}">{v[0]} <span>{v[1]}</span></button>' for s, v in sorted(ALL_TAGS.items(), key=lambda kv: -kv[1][1]))
cat_list = "".join(f'<li><button data-filter="{c}"><span>{CATEGORIAS[c]}</span><em>{CAT_COUNT[c]}</em></button></li>' for c in CATEGORIAS if CAT_COUNT[c])
noticias_index = dict(
    title="Noticias | Consejo Nacional de Mujeres del Perú",
    desc="Noticias, ceremonias, historia y actividades del Consejo Nacional de Mujeres del Perú. Busca por categoría o etiqueta.",
    path="noticias.html",
    body=page_hero("Noticias", "Ceremonias, actividades, historia y novedades de la vida institucional del Consejo.", "img/fotos/contacto-hero.jpg", "Noticias") + f'''
        <section class="section" id="noticias" data-news>
            <div class="container">
                <div class="news-toolbar reveal">
                    <div class="chips">{cat_chips}</div>
                    <label class="search"><i class="fas fa-magnifying-glass"></i><input type="search" id="buscador" placeholder="Buscar noticias…" aria-label="Buscar noticias" autocomplete="off"></label>
                </div>
                <div class="news-layout">
                    <div>
                        <p class="news-count" aria-live="polite"></p>
                        <div class="news-grid">
{"".join(news_card(n) for n in NOTICIAS)}                        </div>
                        <div class="empty" hidden><i class="far fa-newspaper"></i><p>No encontramos noticias con ese criterio.</p><button class="btn btn--outline btn--sm" data-clear>Limpiar filtros</button></div>
                    </div>
                    <aside class="sidebar">
                        <div class="widget">
                            <h4>Categorías</h4>
                            <ul class="cat-list">{cat_list}</ul>
                        </div>
                        <div class="widget">
                            <h4>Etiquetas</h4>
                            <div class="tag-cloud">{tag_cloud}</div>
                        </div>
                        <div class="widget widget--azul">
                            <h4>Actividad permanente</h4>
                            <p><strong>Rezo del Rosario</strong><br>Primeros sábados de cada mes, 5:00 p.m.<br>Plaza del Rosario, av. Salaverry cdra. 6, Jesús María.</p>
                            <a class="btn btn--white btn--sm" href="noticias/rezo-del-rosario-primeros-sabados.html">Más información</a>
                        </div>
                        <div class="widget">
                            <h4>Síguenos</h4>
                            <p>Las novedades del Consejo también en nuestra página de Facebook.</p>
                            <div class="btn-group"><a class="btn btn--azul btn--sm" href="{FB}" target="_blank" rel="noopener noreferrer"><i class="fab fa-facebook-f"></i> Facebook</a><a class="btn btn--outline btn--sm" href="contacto.html?asunto=prensa"><i class="fas fa-envelope"></i> Escríbenos</a></div>
                        </div>
                    </aside>
                </div>
            </div>
        </section>
''' + cta())
with open(os.path.join(ROOT, "noticias.html"), "w", encoding="utf-8") as f:
    f.write(head(noticias_index["title"], noticias_index["desc"], noticias_index["path"]) + header() + noticias_index["body"] + footer())
print("wrote noticias.html")

def article_page(n, idx):
    rel = "../"
    tags = "".join(f'<a class="tag" href="{rel}noticias.html?etiqueta={s}">{tg}</a>' for tg, s in zip(n["tags"], n["tag_slugs"]))
    url = SITE + n["url"]; img = SITE + n["image"]
    related = [m for m in NOTICIAS if m["slug"] != n["slug"] and (m["cat"] == n["cat"] or set(m["tag_slugs"]) & set(n["tag_slugs"]))]
    related += [m for m in NOTICIAS if m["slug"] != n["slug"] and m not in related]
    related = related[:3]
    prev_ = NOTICIAS[idx - 1] if idx > 0 else None
    next_ = NOTICIAS[idx + 1] if idx < len(NOTICIAS) - 1 else None
    def navlink(m, cls, label):
        if not m: return '<span class="post-nav__item post-nav__item--empty"></span>'
        return f'<a class="post-nav__item {cls}" href="{m["slug"]}.html"><span>{label}</span><strong>{m["title"]}</strong></a>'
    share_text = n["title"].replace('"', "").replace("&", "y")
    schema = f'''    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": {json_s(n["title"])},
        "description": {json_s(n["excerpt"])},
        "image": ["{img}"],
        "datePublished": "{n['date']}",
        "dateModified": "{n['date']}",
        "articleSection": "{CATEGORIAS[n['cat']]}",
        "keywords": {json_s(", ".join(n["tags"]))},
        "inLanguage": "es-PE",
        "mainEntityOfPage": {{ "@type": "WebPage", "@id": "{url}" }},
        "author": {{ "@type": "Organization", "name": "Consejo Nacional de Mujeres del Perú", "url": "{SITE}" }},
        "publisher": {{ "@type": "Organization", "name": "Consejo Nacional de Mujeres del Perú", "logo": {{ "@type": "ImageObject", "url": "{SITE}img/logo-512.png" }} }}
    }}
    </script>
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {{ "@type": "ListItem", "position": 1, "name": "Inicio", "item": "{SITE}" }},
            {{ "@type": "ListItem", "position": 2, "name": "Noticias", "item": "{SITE}noticias.html" }},
            {{ "@type": "ListItem", "position": 3, "name": {json_s(n["title"])}, "item": "{url}" }}
        ]
    }}
    </script>
    <meta property="article:published_time" content="{n['date']}">
    <meta property="article:section" content="{CATEGORIAS[n['cat']]}">
''' + "".join(f'    <meta property="article:tag" content="{tg}">\n' for tg in n["tags"])
    cats_side = "".join(f'<li><a href="{rel}noticias.html?categoria={c}"><span>{CATEGORIAS[c]}</span><em>{CAT_COUNT[c]}</em></a></li>' for c in CATEGORIAS if CAT_COUNT[c])
    body = f'''        <section class="post-hero">
            <div class="container">
                <nav class="breadcrumb" aria-label="Ruta"><a href="{rel}index.html">Inicio</a><span>/</span><a href="{rel}noticias.html">Noticias</a><span>/</span><span>{CATEGORIAS[n['cat']]}</span></nav>
                <a class="post__cat" href="{rel}noticias.html?categoria={n['cat']}">{CATEGORIAS[n['cat']]}</a>
                <h1>{n['title']}</h1>
                <p class="post__excerpt">{n['excerpt']}</p>
                <div class="post__meta"><span><i class="far fa-calendar"></i> {n['date_text']}</span><span><i class="far fa-clock"></i> {n['minutes']} min de lectura</span><span><i class="fas fa-building-columns"></i> Consejo Nacional de Mujeres del Perú</span></div>
            </div>
        </section>
        <article class="section post">
            <div class="container">
                <figure class="post__figure reveal">
                    <img src="{rel}{n['image']}" alt="{n['image_alt']}" fetchpriority="high">
                    <figcaption>{n['image_alt']}. Fotografía: {n['credit']}.</figcaption>
                </figure>
                <div class="post__layout">
                    <div class="post__body reveal">
{n['body']}
                        <div class="post__tags"><span>Etiquetas:</span>{tags}</div>
                        <div class="share">
                            <span>Compartir</span>
                            <a href="https://www.facebook.com/sharer/sharer.php?u={url}" target="_blank" rel="noopener noreferrer" aria-label="Compartir en Facebook"><i class="fab fa-facebook-f"></i></a>
                            <a href="https://wa.me/?text={share_text}%20{url}" target="_blank" rel="noopener noreferrer" aria-label="Compartir por WhatsApp"><i class="fab fa-whatsapp"></i></a>
                            <a href="https://twitter.com/intent/tweet?text={share_text}&url={url}" target="_blank" rel="noopener noreferrer" aria-label="Compartir en X"><i class="fab fa-x-twitter"></i></a>
                            <a href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener noreferrer" aria-label="Compartir en LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                            <button type="button" data-copy="{url}" aria-label="Copiar enlace"><i class="fas fa-link"></i></button>
                        </div>
                    </div>
                    <aside class="sidebar reveal reveal-delay-1">
                        <div class="widget widget--azul">
                            <h4>Sobre el Consejo</h4>
                            <p>Asociación civil sin fines de lucro fundada el 3 de marzo de 1923, afiliada al Consejo Internacional de Mujeres desde 1926.</p>
                            <a class="btn btn--white btn--sm" href="{rel}nosotros.html">Conócenos</a>
                        </div>
                        <div class="widget">
                            <h4>Categorías</h4>
                            <ul class="cat-list">{cats_side}</ul>
                        </div>
                        <div class="widget">
                            <h4>Participa</h4>
                            <p>Afíliate como asociada o integra a tu asociación al Consejo.</p>
                            <a class="btn btn--primary btn--sm" href="{rel}participa.html">Quiero participar</a>
                        </div>
                    </aside>
                </div>
                <nav class="post-nav" aria-label="Más noticias">{navlink(prev_, "post-nav__item--prev", "Anterior")}{navlink(next_, "post-nav__item--next", "Siguiente")}</nav>
            </div>
        </article>
        <section class="section section--crema">
            <div class="container">
                <div class="section__header section__header--left reveal"><span class="eyebrow">Noticias relacionadas</span><h2>También te puede interesar</h2></div>
                <div class="news-grid news-grid--3">
{"".join(news_card(m, rel) for m in related)}                </div>
                <div class="mt-32"><a class="btn btn--outline" href="{rel}noticias.html"><i class="fas fa-arrow-left"></i> Volver a noticias</a></div>
            </div>
        </section>
''' + cta(rel)
    return head(n["title"] + " | Consejo Nacional de Mujeres del Perú", n["excerpt"], n["url"], schema, rel=rel, og_image=img, og_type="article") + header(rel) + body + footer(rel)

os.makedirs(os.path.join(ROOT, "noticias"), exist_ok=True)
for i, n in enumerate(NOTICIAS):
    with open(os.path.join(ROOT, n["url"]), "w", encoding="utf-8") as f:
        f.write(article_page(n, i))
    print("wrote", n["url"])

# ---- sitemap y feed RSS
today = datetime.date.today().isoformat()
static_pages = [("", "1.0", "weekly"), ("nosotros.html", "0.9", "monthly"), ("que-hacemos.html", "0.8", "monthly"), ("noticias.html", "0.8", "weekly"), ("participa.html", "0.8", "monthly"), ("contacto.html", "0.6", "yearly"), ("creditos.html", "0.3", "yearly")]
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
for path, pr, ch in static_pages:
    sm.append(f'    <url><loc>{SITE}{path}</loc><lastmod>{today}</lastmod><changefreq>{ch}</changefreq><priority>{pr}</priority></url>')
for n in NOTICIAS:
    sm.append(f'    <url><loc>{SITE}{n["url"]}</loc><lastmod>{n["date"]}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority><image:image><image:loc>{SITE}{n["image"]}</image:loc><image:title>{n["title"].replace("&", "&amp;")}</image:title></image:image></url>')
sm.append('</urlset>')
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n"); print("wrote sitemap.xml")
def rfc(d): return format_datetime(datetime.datetime.fromisoformat(d).replace(tzinfo=datetime.timezone(datetime.timedelta(hours=-5))))
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
items = "".join(f'''
    <item>
      <title>{esc(n["title"])}</title>
      <link>{SITE}{n["url"]}</link>
      <guid isPermaLink="true">{SITE}{n["url"]}</guid>
      <pubDate>{rfc(n["date"])}</pubDate>
      <category>{CATEGORIAS[n["cat"]]}</category>
      <description>{esc(n["excerpt"])}</description>
    </item>''' for n in NOTICIAS)
feed = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Noticias · Consejo Nacional de Mujeres del Perú</title>
    <link>{SITE}noticias.html</link>
    <atom:link href="{SITE}feed.xml" rel="self" type="application/rss+xml"/>
    <description>Ceremonias, actividades, historia y novedades del Consejo Nacional de Mujeres del Perú.</description>
    <language>es-pe</language>
    <lastBuildDate>{rfc(today)}</lastBuildDate>{items}
  </channel>
</rss>
'''
open(os.path.join(ROOT, "feed.xml"), "w", encoding="utf-8").write(feed); print("wrote feed.xml")
