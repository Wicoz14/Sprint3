function validar_formulario() {
    let nombres = document.getElementById("nombres").value
    let apellidos = document.getElementById("apellidos").value
    let selector = document.getElementById("selector").value
    let fecha = document.getElementById("fecha").value
    let celular = document.getElementById("celular").value
    let correo = document.getElementById("email").value
    let confirmarcorreo = document.getElementById("confirmaremail").value
    let contraseña = document.getElementById("contraseña").value
    let confirmarcontraseña = document.getElementById("confirmaremail").value
    let datos = document.getElementById("datos").checked
    let datos1 = document.getElementById("gridCheck").checked


    let sw = true

    if (nombres.length < 1) {
        alert("los nombres están vacíos")
        sw = false
    }
        
    if (apellidos.length < 1) {
        alert("los apellidos están vacíos")
        sw = false
    }

    if (selector=="Choose...") {
        alert("Debe escoger un tipo de documento")
        sw = false
    }

    if (celular.length < 1) {
        alert("el número de celular está vacío")
        sw = false
    }else if (celular.length < 10) {
        alert("el número de celular debe tener 10 números")
        sw = false
    }  

    if (contraseña.length < 1) {
        alert("la contraseña está vacia")
        sw = false
    } else if (contraseña.length < 8) {
        alert("la contraseña debe tener más de 7 caracteres")
        sw = false
    }


    if (correo.length < 1) {
        alert("el correo esta vacío")
        sw = false
    } else {
        if (correo.includes("@")) {
            let separador = correo.split("@")
            let usuario = separador[0]
            if (usuario.length < 1) {
                alert("el correo no tiene el usuario")
                sw = false
            } else {
                let nombreDominio = separador[1]
                if (nombreDominio.includes(".")) {
                    separador = nombreDominio.split(".")
                    let dominio = separador[0]
                    let extension = separador[1]
                    if (dominio.length < 1) {
                        alert("el correo no tiene dominio")
                        sw = false
                    }

                    if (extension.length < 1) {
                        alert("el correo no tiene extension")
                        sw = false
                    }
                } else {
                    alert("el correo no tiene el .")
                    sw = false
                }
            }
        } else {
            alert("el correo no tiene el @")
            sw = false
        }
    }

    
    return sw
}