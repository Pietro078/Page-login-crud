const input_senha = document.getElementById('input_senha')
const btn_senha= document.getElementById('btn_senha')

btn_senha.addEventListener('click',()=>{
    alert('ola')
})

function alerta(){
    return alert('ola')
}

function mostrar(){
    
    if(input_senha.type==='password'){
        input_senha.setAttribute('type','text')
    }

}


