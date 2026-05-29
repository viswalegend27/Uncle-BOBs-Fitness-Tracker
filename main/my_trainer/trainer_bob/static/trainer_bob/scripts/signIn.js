// Activate Lucide icons
lucide.createIcons();

// Toggle password visibility
document.getElementById('togglePw').addEventListener('click', () => {
  const pw = document.getElementById('password');
  const icon = document.querySelector('#togglePw svg');
  if (pw.type === 'password') {
    pw.type = 'text';
    icon.setAttribute('data-lucide', 'eye-off');
  } else {
    pw.type = 'password';
    icon.setAttribute('data-lucide', 'eye');
  }
  lucide.createIcons();
});