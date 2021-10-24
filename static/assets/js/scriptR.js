// evento clik de las optines de menu
document.getElementById("btn_open").addEventListener("click", open_close_menu);

var side_menu = document.getElementById("menu__side")
/* var btn_open = document.getElementById("btn_open") */
var body = document.getElementById("body")
var logo = document.getElementById("logo")
var logoFoot=document.getElementById("logo_foot")
var nombre = document.getElementById("nombre")

function show_name(){
    if (nombre.style.visibility == "visible"){  
        nombre.style.visibility = "hidden"
        
          
    }else{
        nombre.style.visibility="visible";    
    }   
}

function open_close_menu(){
    body.classList.toggle("body_move");
    side_menu.classList.toggle("menu__side_move")
    logo.classList.toggle("logo__move"); 
    logoFoot.classList.toggle("logoFoot__move");

    show_name();

}

// Opciones de menu side//

/* 
let n = document.querySelectorAll(".nombreOpcion");
let  U = document.getElementById("usuario")
let  A = document.getElementById("agregarPelicula")
let  P = document.getElementById("peliculas")
let  F = document.getElementById("funciones")

function active(x){
    for(var i = 0; i < 4; i++){ 
        n[i].style.background="#d1b500 ";
    }
    
    n[x].style.background="#FFDF00"; 

    ocultar()

    if(x==0){
        U.style.display="block"
    }
    if(x==1){
        A.style.display="block"
    }
    if(x==2){
        P.style.display="block"
    }
    if(x==3){
        F.style.display="block"
    }
    
}

function ocultar(){
   

    U.style.display="none"
    A.style.display="none"
    P.style.display="none"
    F.style.display="none"

}

document.addEventListener("DOMContentLoaded", ocultar)
 */


// Evento agregar funciones Dashboard//

const formAddFuntion = document.getElementById("add_funcion");

formAddFuntion.addEventListener("submit", add_data)


function clearInputs(){
    document.getElementById("sala").value=" ";
    document.getElementById("hora").value=" ";
    document.getElementById("capacidad").value=" ";
    document.getElementById("pelicula").value=" ";

}

/* btn = document.querySelector(".btn_delete")
btn.addEventListener("click",delete_Row) */

/* function delete_Row(event){
    var nom = document.getElementById("nom")
    console.log(this)
} */

/* 

function add_data(event){
    event.preventDefault();
    let sala = formAddFuntion.querySelector("#sala").value;
    let hora = formAddFuntion.querySelector("#hora").value;
    let capacidad = formAddFuntion.querySelector("#capacidad").value;
    let pelicula = formAddFuntion.querySelector("#pelicula").value;
    ( - let buttons = "<button id='editar'> Editar </button>  <button id='eliminar'> Eliminar </button>" -)

    let tableOfFuncion = document.getElementById("tableOfContentsF");
    
    let newRow = tableOfFuncion.insertRow(-1);

    let newCell = newRow.insertCell(0);
    newCell.textContent = sala ;

    newCell = newRow.insertCell(1);
    newCell.textContent = hora ;

    newCell = newRow.insertCell(2);
    newCell.textContent = capacidad ;

    newCell = newRow.insertCell(3);
    newCell.textContent = pelicula; 


    newEditarCell = newRow.insertCell(4);
    let botonEditar = document.createElement("button");
    botonEditar.textContent = "Editar"
    newEditarCell.appendChild(botonEditar)

    newDeleteCell = newRow.insertCell(5);
    let deleteButton = document.createElement("button");
    deleteButton.textContent = "Eliminar"
    newDeleteCell.appendChild(deleteButton)
    

    clearInputs();
    deleteButton.addEventListener("click", delete_Row)

}

 */

// Evento buscar usuarios Dashboard//




function searchId(i){
    let ID = document.getElementById("searchBox").value;
    let table=document.getElementById("tableOfContentsU");
    let rows = table.rows.length;
    let searchButton = document.getElementById("searchButton")
    
   
    if( i < rows){
        let dataCell = parseInt(table.rows[i].cells[3].innerText)
        if (dataCell != ID) {
            table.rows[i].remove();
            searchId(i);
        }
        else{
             searchId(2); 
        }
    
        
        

    }

    

}









function searchImage(){
    let coverInput =  document.getElementById("file");
    coverInput.click();
    document.getElementById('file').addEventListener('change', archivo, false);

    
}

function archivo(event){
    var files = event.target.files;
    var f = files[0];

    if(f.type.match("image.*")){

    var reader = new FileReader();

    reader.onload = (function(theFile) {
        return function(e) {
          // Insertamos la imagen
         document.getElementById("image").innerHTML = ['<img class="image" src="', e.target.result,'" title="', escape(theFile.name), '"/>'].join('');
        };
    })(f);

    reader.readAsDataURL(f);
   }
}


/* document.getElementById("cover2").addEventListener("onchange", function(){
    const img = document.getElementsByClassName("image");
    const file = this.files[0];
    if(file){
        const reader = new FileReader();    
        reader.onload=function(){
            const result = reader.result;
            img.src = result;
        }
    reader.readerAsDataURL(file);
    }

}) */













