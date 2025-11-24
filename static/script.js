document.addEventListener("DOMContentLoaded", function () {

    // Tambahkan animasi pada tombol saat form disubmit
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", function () {
            const btn = form.querySelector("button[type=submit]");
            if (btn) {
                btn.innerHTML = "Processing...";
                btn.disabled = true;
            }
        });
    }

    // Attach fillExample to window to ensure it is accessible globally
    window.fillExample = function() {
        form.querySelector("input[name='X']").value = 7;
        form.querySelector("input[name='Y']").value = 5;
        form.querySelector("select[name='month']").value = "aug";
        form.querySelector("select[name='day']").value = "fri";
        form.querySelector("input[name='FFMC']").value = 91.0;
        form.querySelector("input[name='DMC']").value = 140.0;
        form.querySelector("input[name='DC']").value = 680.0;
        form.querySelector("input[name='ISI']").value = 10.5;
        form.querySelector("input[name='temp']").value = 24.0;
        form.querySelector("input[name='RH']").value = 30.0;
        form.querySelector("input[name='wind']").value = 4.0;
        form.querySelector("input[name='rain']").value = 0.0;
    };

});
