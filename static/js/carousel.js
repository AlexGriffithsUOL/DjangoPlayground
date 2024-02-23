document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.getElementById("carousel");
    const items = document.querySelectorAll("#carousel > div");
    const itemWidth = items[0].offsetWidth;
    let currentPosition = 0;
  
    function moveCarousel() {
      currentPosition = (currentPosition + itemWidth) % (itemWidth * items.length);
      carousel.style.transform = `translateX(-${currentPosition}px)`;
    }
  
    setInterval(moveCarousel, 3000); // Change slide every 3 seconds (adjust as needed)
});