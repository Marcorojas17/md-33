document.addEventListener('DOMContentLoaded', () => {
  // Efecto typing en el path del header
  const path = document.querySelector('.header-path');
  if (path) {
    const original = path.textContent;
    path.textContent = '';
    let i = 0;
    const t = setInterval(() => {
      path.textContent = original.slice(0, ++i);
      if (i >= original.length) clearInterval(t);
    }, 28);
  }

  // Reloj UTC en el footer
  const footer = document.querySelector('.site-footer');
  if (footer) {
    const clock = document.createElement('div');
    clock.style.cssText = 'max-width:1080px;margin:16px auto 0;font-size:10px;color:#5c8f6c;letter-spacing:.2em;text-align:center;font-family:monospace';
    footer.appendChild(clock);
    setInterval(() => {
      const d = new Date();
      clock.textContent = `UTC ${d.toISOString().replace('T',' ').slice(0,19)} · TRAZA ACTIVA · SCDR-001`;
    }, 1000);
  }
});