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

// Create account

const goToSignup = document.getElementById("createAccount");
const signIn = document.getElementById("signIn");
const signUp = document.getElementById("signUp");
const backToLogin = document.getElementById("backToLogin");

goToSignup.addEventListener("click", (e) => {
  if (signIn.classList.contains('show')) {
    signUp.classList.replace("hidden", "show");
    signIn.classList.replace("show", "hidden");
  }
});

backToLogin.addEventListener("click", (e) => {
  if (signUp.classList.contains('show')) {
    signIn.classList.replace("hidden", "show");
    signUp.classList.replace("show", "hidden");
  }
});