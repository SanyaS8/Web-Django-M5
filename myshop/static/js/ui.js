document.querySelectorAll('.add-to-cart-form').forEach(form => {
  form.addEventListener('submit', () => {
    const btn = form.querySelector('.btn-buy');
    if (!btn) return;

    btn.classList.add('added');
    btn.textContent = 'Добавлено ✓';

    setTimeout(() => {
      btn.classList.remove('added');
      btn.textContent = 'Добавить в корзину';
    }, 1200);
  });
});
