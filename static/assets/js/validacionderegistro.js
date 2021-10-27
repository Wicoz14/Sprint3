function validarformulario() {
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

    if (nombres.length < 4) {
        alert("Escriba su nombre completo")
        sw = false
    }
        
    if (apellidos.length < 7) {
        alert("Escriba sus apellidos correctamente")
        sw = false
    }

    if (selector=="Choose...") {
        alert("Debe escoger un tipo de documento")
        sw = false
    }

    if (cedula.length < 6) {
        alert("Escriba su documento completo")
        sw = false
    }

    // if (celular.length < 10) {
    //     alert("el número de celular es incorrecto")
    //     sw = false
    // }

    if (contraseña.length < 6) {
        alert("la contraseña debe tener al menos 6 caracteres")
        sw = false
    }

    if (correo!=confirmarcorreo){
        sw= false
        alert("los correos inscritos son distintos en ambos campos")
    }

    console.log(contraseña)
    console.log(confirmarcontraseña)
    if (contraseña!=confirmarcontraseña){
        alert("los contraseñas inscritas son distintas en ambos campos")
        sw= false
    }

    if (sw){
        return true;
    }else{
        return false;
    }
   
}
link = document.querySelector('#formdebusqueda');
	        link.addEventListener('click', function(e) {
	                  valor = document.querySelector('#busquedainput').value;
	                  this.action = '/busqueda/' + valor;
	        });