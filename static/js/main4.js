const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
    
    rif: /^\d{1,14}$/,
    telefono: /^\d{1,14}$/
    
}
const campos = {
    rif: false,
    telefono: false
    
}


const validarFormulario = (e) => {
    switch (e.target.name) {
        case "telefono":
            validarCampo(expresiones.telefono, e.target, "telefono");
            
        break;

        case "rif":
            validarCampo(expresiones.rif, e.target, "rif");
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

    e.preventDefault();
    if (campos.telefono && campos.rif){
        formulario.reset();
        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        setTimeout(() =>{
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
        }, 5000);
    }else{
        document.getElementById('formulario__mensaje-error').classList.add('formulario__mensaje-error-activo');
        setTimeout(() =>{
            document.getElementById('formulario__mensaje-error').classList.remove('formulario__mensaje-error-activo');
        }, 5000);
        
    }
});