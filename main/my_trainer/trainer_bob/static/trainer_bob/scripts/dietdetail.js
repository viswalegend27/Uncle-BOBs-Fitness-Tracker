// explicit declaration of my modal window.
const modal = document.querySelector(".float-window");
const content = document.querySelector(".main-content");
const createBlogBtn = document.querySelector(".create-blog");
const createBlog = document.querySelector(".blog-window");
const blogForm = document.getElementById("blogForm");
// main-content -> content
const blogContent = document.querySelector(".content");

// logic for modal appearence when clicking read-more.
document.querySelectorAll(".read-more").forEach(link => { 
  link.addEventListener("click", function(e) {
  e.preventDefault(); // preventing default reaload anim.
  const title = this.closest(".text-cont").querySelector("h3").innerText; // getting the actual title from the code.
  let contentData = [];

  if (title.toLowerCase().includes("deficit")) {
      contentData = calDef;
  } else if (title.toLowerCase().includes("surplus")) {
      contentData = calSurp;
  }

  const modalContent = document.getElementById("modal-content");
  modalContent.innerHTML = "";

  modalContent.innerHTML = `<p>${contentData}</p>`;
  document.getElementById("output").innerText = title;
  modal.classList.add("show");
  });
});

// logic for create-blog form
createBlogBtn.addEventListener("click", (event) => {
  event.preventDefault();
  createBlog.classList.add("show");
});

// close logic 1 for create-blog form
createBlog.addEventListener("click", (event)=> {
    if (event.target.classList.contains("blog-window")) {
      createBlog.classList.remove("show");
    }
});

// logic for closing create-blog window.
document.querySelector(".blog-close-btn").addEventListener("click", () => {
  // removing my show from previous read-more tab.
  createBlog.classList.remove("show");
  // removing hide from content and enabling content to show.
  content.classList.remove("hide");
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
  }
});

// logic for blog creation
blogForm.addEventListener("submit", async function(event) {
    event.preventDefault();
    const formData = new FormData(this);

    let userInp = {}

    for (const k of formData.keys()) {
        if(formData.get(k).toString().length > 0) {
            userInp[k] = formData.get(k).toString()
        }
    }
    const blogResponse = await fetch("http://127.0.0.1:8000/create-blog/", {
        method: "POST",
        headers: {
            "Content-Type" : "application/json"
        },
        body: JSON.stringify(userInp)
    })    
    const data = await blogResponse.json();
    console.log(data)
})

