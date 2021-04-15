const prev = document.querySelector(".prev");
const next = document.querySelector(".next");
const slides = document.querySelectorAll(".slide");

let currentIndex = 0;

next.addEventListener("click", () => {
  if (currentIndex == slides.length - 1) {
    currentIndex = 0;
    document.querySelector(".active").classList.remove("active");
    slides[currentIndex].classList.add("active");
    return;
  }

  if (currentIndex < slides.length) {
    document.querySelector(".active").classList.remove("active");
    currentIndex++;
    slides[currentIndex].classList.add("active");
  }
});

prev.addEventListener("click", () => {
  if (currentIndex == 0) {
    currentIndex = slides.length - 1;
    document.querySelector(".active").classList.remove("active");
    slides[currentIndex].classList.add("active");
    return;
  }

  if (currentIndex < slides.length) {
    document.querySelector(".active").classList.remove("active");
    currentIndex--;
    slides[currentIndex].classList.add("active");
  }
});