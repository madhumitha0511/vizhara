document.addEventListener('DOMContentLoaded', () => {
  // Gallery lightbox wiring
  document.querySelectorAll('.gallery-thumb').forEach(el=>{
    el.addEventListener('click', ()=>{
      const src = el.getAttribute('data-src') || el.querySelector('img').src;
      const img = document.getElementById('lightbox-img');
      img.src = src;
      var myModal = new bootstrap.Modal(document.getElementById('lightbox'));
      myModal.show();
    });
  });

  // Smooth scroll for anchor links (if present)
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.addEventListener('click', e=>{
      e.preventDefault();
      const target = document.querySelector(a.getAttribute('href'));
      if(target) target.scrollIntoView({behavior:'smooth'});
    });
  });

  // Small animation: fade in buttons after load
  setTimeout(()=> {
    document.querySelectorAll('.animate__animated').forEach(el=>{
      el.classList.add('animate__fadeInUp');
    });
  }, 400);
});
