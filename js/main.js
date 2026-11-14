/* Consejo Nacional de Mujeres del Perú — interacciones */
document.documentElement.classList.add('js');
(function () {
    'use strict';

    // Menú móvil
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.querySelector('.nav');
    if (toggle && nav) {
        toggle.addEventListener('click', function () {
            var open = nav.classList.toggle('is-open');
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
        nav.querySelectorAll('a').forEach(function (a) {
            a.addEventListener('click', function () {
                nav.classList.remove('is-open');
                toggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    // Enlace activo según página
    var current = location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav__list a').forEach(function (a) {
        var href = a.getAttribute('href');
        if (href === current || (current === '' && href === 'index.html')) a.classList.add('is-active');
    });

    // Sombra del header y botón volver arriba
    var header = document.querySelector('.header');
    var backTop = document.querySelector('.back-top');
    function onScroll() {
        var y = window.scrollY || window.pageYOffset;
        if (header) header.classList.toggle('is-scrolled', y > 10);
        if (backTop) backTop.classList.toggle('is-visible', y > 600);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
    if (backTop) backTop.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });

    // Animaciones al hacer scroll
    var reveals = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window && reveals.length) {
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (e) {
                if (e.isIntersecting) { e.target.classList.add('is-visible'); io.unobserve(e.target); }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
        reveals.forEach(function (el) { io.observe(el); });
    } else {
        reveals.forEach(function (el) { el.classList.add('is-visible'); });
    }

    // Acordeón de preguntas frecuentes
    document.querySelectorAll('.faq__q').forEach(function (btn) {
        btn.addEventListener('click', function () {
            var item = btn.closest('.faq__item');
            var open = item.classList.toggle('is-open');
            btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        });
    });

    // Año actual
    document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

    // Formulario de contacto
    var form = document.querySelector('form[data-ajax]');
    if (form) {
        var status = form.querySelector('.form__status');
        var submitBtn = form.querySelector('button[type="submit"]');
        form.addEventListener('submit', function (ev) {
            ev.preventDefault();
            status.className = 'form__status';
            var original = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Enviando…';
            fetch(form.getAttribute('action'), { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
                .then(function (r) { return r.json().catch(function () { return { ok: false }; }); })
                .then(function (data) {
                    if (data && data.ok) {
                        status.textContent = data.message || 'Gracias, recibimos tu mensaje. Te responderemos pronto.';
                        status.classList.add('is-ok');
                        form.reset();
                    } else {
                        status.textContent = (data && data.message) || 'No pudimos enviar el mensaje. Inténtalo de nuevo o escríbenos por correo.';
                        status.classList.add('is-error');
                    }
                })
                .catch(function () {
                    status.textContent = 'No pudimos enviar el mensaje. Inténtalo de nuevo o escríbenos por correo.';
                    status.classList.add('is-error');
                })
                .finally(function () { submitBtn.disabled = false; submitBtn.innerHTML = original; });
        });
    }
})();

/* Preselecciona el motivo del formulario desde la URL (?asunto=afiliacion) */
(function () {
    var sel = document.getElementById('asunto');
    if (!sel) return;
    var m = /[?&]asunto=([a-z]+)/.exec(location.search);
    if (m && sel.querySelector('option[value="' + m[1] + '"]')) sel.value = m[1];
})();

/* Noticias: enlace activo en subpáginas, filtros, buscador y copiar enlace */
(function () {
    if (location.pathname.indexOf('/noticias/') !== -1) {
        document.querySelectorAll('.nav__list a').forEach(function (a) { if (/noticias\.html$/.test(a.getAttribute('href'))) a.classList.add('is-active'); });
    }
    document.querySelectorAll('[data-copy]').forEach(function (b) {
        b.addEventListener('click', function () {
            var url = b.getAttribute('data-copy');
            (navigator.clipboard ? navigator.clipboard.writeText(url) : Promise.reject()).then(function () {
                b.classList.add('is-copied'); b.innerHTML = '<i class="fas fa-check"></i>';
                setTimeout(function () { b.classList.remove('is-copied'); b.innerHTML = '<i class="fas fa-link"></i>'; }, 1800);
            }).catch(function () { window.prompt('Copia el enlace:', url); });
        });
    });
    var root = document.querySelector('[data-news]');
    if (!root) return;
    var cards = Array.prototype.slice.call(root.querySelectorAll('.news-card'));
    var input = root.querySelector('#buscador');
    var count = root.querySelector('.news-count');
    var empty = root.querySelector('.empty');
    var state = { cat: 'todas', tag: '', q: '' };
    function norm(s) { return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }
    function apply() {
        var shown = 0;
        cards.forEach(function (c) {
            var okCat = state.cat === 'todas' || c.getAttribute('data-category') === state.cat;
            var okTag = !state.tag || (',' + c.getAttribute('data-tags') + ',').indexOf(',' + state.tag + ',') !== -1;
            var okQ = !state.q || norm(c.getAttribute('data-search')).indexOf(norm(state.q)) !== -1;
            var ok = okCat && okTag && okQ;
            c.classList.toggle('is-hidden', !ok); if (ok) shown++;
        });
        root.querySelectorAll('[data-filter]').forEach(function (b) { b.classList.toggle('is-active', b.getAttribute('data-filter') === state.cat); });
        root.querySelectorAll('[data-tag]').forEach(function (b) { b.classList.toggle('is-active', b.getAttribute('data-tag') === state.tag); });
        var parts = [];
        if (state.cat !== 'todas') { var cb = root.querySelector('.chip[data-filter="' + state.cat + '"]'); parts.push('categoría «' + (cb ? cb.firstChild.textContent.trim() : state.cat) + '»'); }
        if (state.tag) { var tb = root.querySelector('[data-tag="' + state.tag + '"]'); parts.push('etiqueta «' + (tb ? tb.firstChild.textContent.trim() : state.tag) + '»'); }
        if (state.q) parts.push('búsqueda «' + state.q + '»');
        count.textContent = 'Mostrando ' + shown + ' de ' + cards.length + ' noticias' + (parts.length ? ' · ' + parts.join(', ') : '');
        empty.hidden = shown !== 0;
        var qs = [];
        if (state.cat !== 'todas') qs.push('categoria=' + state.cat);
        if (state.tag) qs.push('etiqueta=' + state.tag);
        if (state.q) qs.push('q=' + encodeURIComponent(state.q));
        history.replaceState(null, '', location.pathname + (qs.length ? '?' + qs.join('&') : ''));
    }
    root.querySelectorAll('[data-filter]').forEach(function (b) { b.addEventListener('click', function () { state.cat = b.getAttribute('data-filter'); apply(); }); });
    root.querySelectorAll('[data-tag]').forEach(function (b) { b.addEventListener('click', function () { state.tag = state.tag === b.getAttribute('data-tag') ? '' : b.getAttribute('data-tag'); apply(); }); });
    root.querySelectorAll('.news-card .tag').forEach(function (a) { a.addEventListener('click', function (e) { e.preventDefault(); state.tag = /etiqueta=([a-z0-9-]+)/.exec(a.getAttribute('href'))[1]; apply(); window.scrollTo({ top: root.offsetTop - 100, behavior: 'smooth' }); }); });
    root.querySelectorAll('[data-clear]').forEach(function (b) { b.addEventListener('click', function () { state = { cat: 'todas', tag: '', q: '' }; input.value = ''; apply(); }); });
    var timer; input.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(function () { state.q = input.value.trim(); apply(); }, 150); });
    var m;
    if ((m = /[?&]categoria=([a-z]+)/.exec(location.search))) state.cat = m[1];
    if ((m = /[?&]etiqueta=([a-z0-9-]+)/.exec(location.search))) state.tag = m[1];
    if ((m = /[?&]q=([^&]+)/.exec(location.search))) { state.q = decodeURIComponent(m[1]); input.value = state.q; }
    apply();
})();
