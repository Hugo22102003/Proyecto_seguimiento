const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
    
    firmante: /^[a-zA-ZÁ-ÿ\s]{1,40}$/,
    numero: /^\d{1,14}$/
    
}



const validarFormulario = (e) => {
    switch (e.target.name) {
        case "firmante":
            validarCampo(expresiones.firmante, e.target, "firmante")
            
        break;

        case "numero":
            validarCampo(expresiones.numero, e.target, "numero")
        break;
    }
    
}

const validarCampo = (expresion, input, campo) =>{
    if(expresion.test(input.value)){
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[campo] = true;
    } else {
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos[campo] = false;
    }
}

inputs.forEach((input) =>{
    input.addEventListener('keyup', validarFormulario );
    input.addEventListener('blur', validarFormulario );
});

formulario.addEventListener('submit', (e) => {
    
    if (campos.firmante && campos.numero){
        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        setTimeout(() =>{
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
        }, 5000);
        formulario.reset(); 
    }else{
        document.getElementById('formulario__mensaje-error').classList.add('formulario__mensaje-error-activo');
        setTimeout(() =>{
            document.getElementById('formulario__mensaje-error').classList.remove('formulario__mensaje-error-activo');
        }, 5000);
        e.preventDefault();
        
    }
});