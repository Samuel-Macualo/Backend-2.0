function validateName(input) {
    const regex = /^[A-Za-z\s]+$/;
    if (!regex.test(input.value)) {
        alert("El nombre solo puede contener letras y espacios.");
        input.value = "";
    }
}

function validatePhone(input) {
    const regex = /^[0-9]{10}$/;
    if (!regex.test(input.value)) {
        alert("El número de teléfono debe contener exactamente 10 dígitos.");
        input.value = "";
    }
}
function validateEmail(input) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!regex.test(input.value)) {
        alert("Por favor, ingrese un correo electrónico válido.");
        input.value = "";
    }
}

function validatePassword(input, username) {
    const password = input.value;
    const usernameLower = username.toLowerCase();
    const hasUpperCase = /[A-Z]/.test(password);
    const hasNumber = /[0-9]/.test(password);
    const noConsecutiveNumbers = !/(\d)\1{2}/.test(password); // Evita 3 números consecutivos iguales
    const containsUsername = password.toLowerCase().includes(usernameLower);

    if (!hasUpperCase) {
        alert("La contraseña debe contener al menos una letra mayúscula.");
        input.value = "";
    } else if (!hasNumber) {
        alert("La contraseña debe contener al menos un número.");
        input.value = "";
    } else if (!noConsecutiveNumbers) {
        alert("La contraseña no puede tener números consecutivos iguales.");
        input.value = "";
    } else if (containsUsername) {
        alert("La contraseña no puede contener el nombre de usuario.");
        input.value = "";
    }
}
