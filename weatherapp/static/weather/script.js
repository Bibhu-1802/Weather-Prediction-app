document.addEventListener("DOMContentLoaded", () => {
    console.log("Weather App Ready 🚀");

    const form = document.querySelector("form");
    const card = document.querySelector(".card");

    if (form) {
        form.addEventListener("submit", () => {
            if (card) {
                card.classList.remove("fade-in");
                setTimeout(() => {
                    card.classList.add("fade-in");
                }, 100);
            }
        });
    }
});

