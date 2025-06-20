document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("surpriseForm");
    const nameInput = document.getElementById("name");
    form.addEventListener("submit", function() {
        localStorage.setItem("surpriseName", nameInput.value);
    });
    // Autofill name if previously entered
    const savedName = localStorage.getItem("surpriseName");
    if (savedName && !nameInput.value) {
        nameInput.value = savedName;
    }
});