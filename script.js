// script.js

// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {

    // Hamburger menu functionality
    const hamburger = document.getElementById("hamburger");
    const navLinks = document.querySelector(".navbar-right .nav-links");

    hamburger.addEventListener("click", function () {
        navLinks.classList.toggle("active");
    });

    // Chatbot functionality
    const sendMessage = async () => {
        const userInput = document.getElementById('userInput').value;

        // Send POST request to the backend
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userInput })
        });

        // Get the response from the backend
        const data = await response.json();

        // Display the response message in the HTML
        document.getElementById('response').innerText = data.message;
    };

    // Attach the sendMessage function to the "Send" button
    const sendButton = document.querySelector("button");
    sendButton.addEventListener("click", sendMessage);
});
