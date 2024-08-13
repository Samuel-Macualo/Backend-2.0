document.addEventListener('DOMContentLoaded', function () {
    // Selecciona todos los formularios de eliminación
    const deleteForms = document.querySelectorAll('.delete-form');

    deleteForms.forEach(form => {
        form.addEventListener('submit', function (e) {
            e.preventDefault();  // Evita que el formulario se envíe inmediatamente

            Swal.fire({
                title: '¿Estás seguro?',
                text: "¡No podrás revertir esta acción!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#d33',
                cancelButtonColor: '#3085d6',
                confirmButtonText: 'Sí, eliminar',
                cancelButtonText: 'Cancelar'
            }).then((result) => {
                if (result.isConfirmed) {
                    form.submit();  // Envía el formulario si el usuario confirma
                }
            });
        });
    });
});

document.getElementById('search-button').addEventListener('click', function() {
    const searchColumn = document.getElementById('search-column').value;
    const searchQuery = document.getElementById('search-query').value.trim();

    if (!searchColumn || !searchQuery) {
        Swal.fire({
            icon: 'warning',
            title: 'Campo vacío',
            text: 'Por favor seleccione una columna y llene el campo de búsqueda.',
        });
    } else {
        // Aquí puedes implementar la lógica de la búsqueda,
        // por ejemplo redireccionar con parámetros de consulta en la URL
        // window.location.href = `?${searchColumn}=${searchQuery}`;
    }
});

