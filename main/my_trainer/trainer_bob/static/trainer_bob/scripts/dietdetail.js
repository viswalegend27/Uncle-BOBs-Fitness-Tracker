// explicit declaration of my modal window.
const modal = document.querySelector(".float-window");
const content = document.querySelector(".main-content");


// logic for modal appearence when clicking read-more.
document.querySelectorAll(".read-more").forEach(link => { 
  link.addEventListener("click", function(e) {
  e.preventDefault();
  const title = this.closest(".text-cont").querySelector("h3").innerText;
  let contentData = [];

  if (title.toLowerCase().includes("deficit")) {
      contentData = calDef;
  } else if (title.toLowerCase().includes("surplus")) {
      contentData = calSurp;
  }

  const modalContent = document.getElementById("modal-content");
  modalContent.innerHTML = "";

  contentData.forEach(item => {
    modalContent.innerHTML += `<p>• ${item}</p>`;
  });
  document.getElementById("output").innerText = title;
  content.classList.add("show");
  modal.classList.add("show");
  });
});

// logic for close-btn inside modal to reappear the actual window.
document.querySelector(".close-btn").addEventListener("click", () => {
  // removing my show from previous read-more tab.
  modal.classList.remove("show");
  // removing hide from content and enabling content to show.
  content.classList.remove("hide");
});

// clicking logic for closing the windows.
document.querySelector(".float-window").addEventListener("click", (e) => {
  if (e.target.classList.contains("float-window")) {
    modal.classList.remove("show");
    content.classList.remove("hide");
    content.classList.add("show");
  }
});