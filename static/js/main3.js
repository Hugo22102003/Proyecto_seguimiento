const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
    
    nombre: /^[a-zA-ZÁ-ÿ\s]{1,40}$/,
    cedula: /^\d{1,14}$/, 
    telefono: /^\d{1,14}$/,
    tipo: /^[a-zA-ZÁ-ÿ\s]{1,40}$/

    
}
const campos = {
    nombre: false,
    cedula: false,
    telefono: false,
    tipo: false,
}



const validarFormulario = (e) => {
    switch (e.target.name) {
        case "nombre":
            validarCampo(expresiones.nombre, e.target, "nombre");
            
        break;

        case "cedula":
            validarCampo(expresiones.cedula, e.target, "cedula");
        break;

        case "telefono":
            validarCampo(expresiones.telefono, e.target, "telefono");
        break;

        case "tipo":
            validarCampo(expresiones.tipo, e.target, "tipo");
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
    if (campos.nombre && campos.cedula && campos.telfono && campos.tipo ){
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