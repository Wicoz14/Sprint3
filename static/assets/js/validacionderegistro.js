function validar_formulario() {
    let nombres = document.getElementById("nombres").value
    let apellidos = document.getElementById("apellidos").value
    let selector = document.getElementById("selector").value
    let celular = document.getElementById("celular").value
    let correo = document.getElementById("email").value
    let confirmarcorreo = document.getElementById("confirmaremail").value
    let contraseña = document.getElementById("contraseña").value
    let confirmarcontraseña = document.getElementById("confirmarcontraseña").value
    let cedula = document.getElementById("doc").value

    let sw = true

    if (selector=="Choose...") {
        alert("Debe escoger un tipo de documento")
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

    if (correo =! confirmarcorreo){
        alert("los correos inscritos son distintos en ambos campos")
        sw = false
    }

    if (contraseña =! confirmarcontraseña){
        alert("los contraseñas inscritas son distintas en ambos campos")
        sw = false
    }

    return sw
}