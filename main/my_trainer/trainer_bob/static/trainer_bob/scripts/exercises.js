// getting my dropdown btn ✅
const dropdownButton = document.getElementById('dropdownButton');
const dropdownContent = document.getElementById('dropdownContent');

// hamburger and dropdown dynamic UI logic
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('nav ul');
const dropdown = document.querySelector('.dropdown');

hamburger.addEventListener('click', ()=> {
  hamburger.classList.toggle('hamburger-active');
  navMenu.classList.toggle('active');
});

dropdown.addEventListener('click', () => {
  if (window.innerWidth <= 790) {
    dropdown.classList.toggle('active');
  }
});

// creating my click listener for for drop down clickd ✅
dropdownButton.addEventListener('click', ()=> {
  dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
});

// closing the dropdwn if user clicks outside
window.addEventListener('click', (e) => {
  if (!e.target.matches('.dropdown button')) {
    dropdownContent.style.display = 'none';
  }
})