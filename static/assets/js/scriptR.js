// evento clik de las optines de menu
document.getElementById("btn_open").addEventListener("click", open_close_menu);

var side_menu = document.getElementById("menu__side")

var body = document.getElementById("body")
var logo = document.getElementById("logo")
var logoFoot=document.getElementById("logo_foot")
var nombre = document.getElementById("nombre")


var caratula = document.getElementById("caratula")

var menuLogin = document.getElementById("menu_login")


function alertaDeVacio(){
var name = document.getElementById("name").required = true;
var duration = document.getElementById("duration").required = true;
var director = document.getElementById("director").required = true;
var genre = document.getElementById("genre").required = true;
var trailer = document.getElementById("trailer").required = true;
var estreno = document.getElementById("estreno").required = true;
var actors = document.getElementById("actors").required = true;
var textSynopsis = document.getElementById("textSynopsis").required = true;
var file = document.getElementById("file").required = true;
var file_pancarta = document.getElementById("file_pancarta").required = true;

console.log(file)
return(window.alert("Debe llenar todos los campos"))
}


function show(n){
    if (n.style.visibility == "visible"){  
        n.style.visibility = "hidden"
        
          
    }else{
        n.style.visibility="visible";    
    }   
}

function open_close_menu(){
    header.classList.toggle("header_move") 
    body.classList.toggle("body_move");
    side_menu.classList.toggle("menu__side_move")
    logo.classList.toggle("logo__move"); 
    logoFoot.classList.toggle("logoFoot__move");
    
    
    show(nombre);

}

/* window.onload = function() {
    side_menu
};
 */




// Opciones de menu side//


// Evento agregar funciones Dashboard//

const formAddFuntion = document.getElementById("add_funcion");

/* formAddFuntion.addEventListener("submit", add_data) */


function clearInputs(){
    document.getElementById("sala").value=" ";
    document.getElementById("hora").value=" ";
    document.getElementById("capacidad").value=" ";
    document.getElementById("pelicula").value=" ";

}



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
    

    coverInput.addEventListener('change', archivo, false);
    
    
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


function searchImagePancarta(){
  
    let pancartaImput = document.getElementById('file_pancarta')

    
    pancartaImput.click();

   
    pancartaImput.addEventListener('change', archivop, false);
    
}

function archivop(event){
    var filePancarta = event.target.files;

    var p = filePancarta[0]

    if(p.type.match("image.*")){

    var reader = new FileReader();

    reader.onload = (function(theFile) {
        return function(e) {
          // Insertamos la imagen
         document.getElementById("cont_image_pancarta").innerHTML = ['<img class="pancarta" src="', e.target.result,'" title="', escape(theFile.name), '"/>'].join('');
        };
        
    })(p);

    reader.readAsDataURL(p);
   }
}
















