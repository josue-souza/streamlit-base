const initialize = () => {
    const box = document.querySelector("#example-box");
    const button = document.querySelector("#example-button");

    if (!box || !button) {
        return;
    }

    if (button.dataset.jsInitialized === "true") {
        return;
    }

    button.dataset.jsInitialized = "true";

    const colors = ["red", "blue", "green", "purple", "orange"];
    let colorIndex = 0;

    button.addEventListener("click", () => {
        box.style.backgroundColor = colors[colorIndex];
        colorIndex = (colorIndex + 1) % colors.length;
    });
};

initialize();

const observer = new MutationObserver(() => {
    initialize();
});

observer.observe(document.body, {
    childList: true,
    subtree: true
});