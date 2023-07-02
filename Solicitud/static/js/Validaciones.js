

function valida() {
    var nombre = document.getElementById("txtNombre").value;
    var apellido = document.getElementById("txtApellidos").value;
    var email = document.getElementById("txtEmail").value;
    var telefono = document.getElementById("txtTelefono").value;
    



    // Validar nombre
    if (nombre == "" ) {
      alert("Por favor, ingrese su nombre");
      return false;
    }

    if (apellido == "" ) {
        alert("Por favor, ingrese su apellido");
        return false;
      }
    
    // Validar email
    if (email == "") {
      alert("Por favor, ingrese su correo electrónico");
      return false;
    } else {
      var expresion = /\w+@\w+\.[a-z]{2,}$/;
      if (!expresion.test(email)) {
        alert("Por favor, ingrese un correo electrónico válido");
        return false;
      }
    }
    
    

    var expresion = /^\d{10}$/; // Expresión regular que verifica si el teléfono tiene 10 dígitos numéricos
    if (!expresion.test(telefono)) {
        alert("Por favor, ingrese un número de teléfono válido (10 dígitos)");
        return false;
    }
    
    // Si todo está correcto, enviar formulario
    alert("Su mensaje ha sido enviado correctamente");
    return true;
  }
  