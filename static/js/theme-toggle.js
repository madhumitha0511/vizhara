document.addEventListener("DOMContentLoaded", function () {
  const btn = document.getElementById("theme-toggle");
  btn.onclick = () => {
    document.body.classList.toggle("dark-mode");
  };
});
