function cancelamento_rt(){
     container = document.getElementById('form-cancelamento')
     html =                  '<div class = "cancela_rt">'+
                             '<h3>CANCELAMENTO</h3>'+
                             '<span class="btn-add-cancelamento" onclick="cancelamento_rt()"></span>'+
                             '<div id="form-cancelamento">'+
                             '<label for="data_solicitacao">DATA DA SOLICITAÇÃO:</label>'+
                             '<input type="date" id="data_solicitacao" name="data_solicitacao" value="{{data_solicitacao}}"><br>'+
                             '<label for="c_env_presidencia">DATA DE ENVIO A PRESIDÊNCIA:</label>'+
                             '<input type="date" id="c_env_presidencia" name="c_env_presidencia" value="{{c_env_presidencia}}"><br>'+
                             '<label for="c_rec_presidencia">RECEBIDO DA PRESIDÊNCIA:</label>'+
                             '<input type="date" id="c_rec_presidencia" name="c_rec_presidencia" value="{{c_rec_presidencia}}"><br>'+
                             '<label for="decisao">DECISÃO:</label>'+
                             '<input type="text" id="decisao" name="decisao" value="{{decisao}}"><br>'+
                             '</div>'+
                             '</div>'+
                             '<input type="submit" value="Enviar" class="btn-principal" onsubmit="return is_cnpj_valido(cnpj)">'+
                             '</form>'

     container.innerHTML += html

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