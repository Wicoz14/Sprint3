// evento clik de las optines de menu
document.getElementById("btn_open").addEventListener("click", open_close_menu);

var side_menu = document.getElementById("menu__side")
var btn_open = document.getElementById("btn_open")
var body = document.getElementById("body")
var logo = document.getElementById("icon_logo")
var nombre = document.getElementById("nombre")

function nom(){
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

    nom();

}


// Evento agregar funciones Dashboard//

const formAddFuntion = document.getElementById("add_funcion");

formAddFuntion.addEventListener("submit", add_data)


function clearInputs(){
    document.getElementById("sala").value=" ";
    document.getElementById("hora").value=" ";
    document.getElementById("capacidad").value=" ";
    document.getElementById("pelicula").value=" ";

}

function delete_Row(event){
    event.target.parentNode.parentNode.remove();
}



function add_data(event){
    event.preventDefault();
    let sala = formAddFuntion.querySelector("#sala").value;
    let hora = formAddFuntion.querySelector("#hora").value;
    let capacidad = formAddFuntion.querySelector("#capacidad").value;
    let pelicula = formAddFuntion.querySelector("#pelicula").value;
   

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



// Evento buscar usuarios Dashboard//




function searchId(i){
    let ID = document.getElementById("searchBox").value;
    let table=document.getElementById("tableOfContentsU");
    let rows = table.rows.length;
    let searchButton = document.getElementById("searchButton")
    console.log(i)
    console.log(rows)
   
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


let deleteButton = document.getElementById("deleteButton").addEventListener("click", delete_Row)



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







