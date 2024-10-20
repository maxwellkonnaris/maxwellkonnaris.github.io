// script.js

document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.getElementById("hamburger");
    const navLinks = document.querySelector(".navbar-right .nav-links");

    hamburger.addEventListener("click", function () {
        navLinks.classList.toggle("active");
    });
});


