function cancelamento_rt(){
     container = document.getElementById('form-cancelamento')
     container2 = "templates/attform.html"

     container.innerHTML += container2

 }


function exibir_form(tipo){

     add_rt = document.getElementById('adicionar_rt')
     att_rt = document.getElementById('att_rt')

     if(tipo == "1"){
        att_rt.style.display = "none" 
        add_rt.style.display = "block"
     }else if(tipo == "2"){
        add_rt.style.display = "none";
        att_rt.style.display = "block";
     }
}

console.log(adicionar_rt);
console.log(att_rt);