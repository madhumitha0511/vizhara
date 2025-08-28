document.addEventListener("scroll", function(){
  document.querySelectorAll(".animate-in, .animate-up, .animate-fade").forEach(e=>{
    if(window.scrollY + window.innerHeight > e.offsetTop+30) e.classList.add("active");
  })
});
