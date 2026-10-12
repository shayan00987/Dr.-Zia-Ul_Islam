(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
      nav.classList.toggle('open', open);
    });
    nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
      nav.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); toggle.setAttribute('aria-label', 'Open navigation');
    }));
  }
  const year = document.getElementById('year'); if (year) year.textContent = new Date().getFullYear();
  const revealItems = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('is-visible'); observer.unobserve(entry.target); }
    }), { threshold: 0.12 });
    revealItems.forEach(item => observer.observe(item));
  } else revealItems.forEach(item => item.classList.add('is-visible'));
  // Independent, non-repeating photo sequences in two separate sections.
  document.querySelectorAll('.image-cycle').forEach((wrap, index) => {
    let images; try { images = JSON.parse(wrap.dataset.images || '[]'); } catch { images = []; }
    const img = wrap.querySelector('img'); if (!img || images.length < 2) return;
    let current = 0;
    const dots = wrap.querySelectorAll('.cycle-dots i');
    window.setInterval(() => {
      current = (current + 1) % images.length;
      img.style.opacity = '0.15';
      window.setTimeout(() => {
        img.src = images[current]; img.onload = () => { img.style.opacity = '1'; };
        if (wrap.querySelector('.count-current')) wrap.querySelector('.count-current').textContent = String(current + 1).padStart(2, '0');
        dots.forEach((dot, i) => dot.classList.toggle('active', i === current));
      }, 350);
    }, 5200 + index * 300);
  });
})();
