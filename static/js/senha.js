function togglePassword() {
    var passwordField = document.getElementById("senha");
    var toggleButton = document.getElementById("btn_senha");
    if (passwordField.type === "password") {
        passwordField.type = "text";
        toggleButton.textContent = 'ocultar senha'
    } else {
        passwordField.type = "password";
        toggleButton.textContent = 'mostrar senha'
    }
}