const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
    usuario: /^[a-zA-Z0-9\_\-]{4,16}$/,
    nombre: /^[a-zA-ZÁ-ÿ\s]{1,40}$/,
    telefono: /^\d{7,14}$/,
    apellido: /^[a-zA-ZÁ-ÿ\s]{1,40}$/,
    password: /^\d{4,12}$/,
    cargo: /^[a-zA-ZÁ-ÿ\s]{1,40}$/,
    cedula: /^\d{4,12}$/
}

const campos = {
    usuario: false,
    nombre: false,
    telefono: false,
    apellido: false,
    password: false,
    cargo: false, 
    cedula: false
}

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "username":
            validarCampo(expresiones.usuario, e.target, "usuario");
            
        break;

        case "nombre":
            validarCampo(expresiones.nombre, e.target, "nombre");
        
        break;

        case "apellido":
            validarCampo(expresiones.apellido, e.target, "apellido");
        break;

        case "password":
            validarCampo(expresiones.password, e.target, "password");
        break;
        
        case "cargo":
            validarCampo(expresiones.cargo, e.target, "cargo");
        break;

        case "cedula":
            validarCampo(expresiones.cedula, e.target, "cedula");
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
    if(campos.usuario && campos.nombre && campos.apellido && campos.password && campos.cargo && campos.cedula){
        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
        }, 5000);
    }else{
        
        document.getElementById('formulario__mensaje-error').classList.add('formulario__mensaje-error-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje-error').classList.remove('formulario__mensaje-error-activo');
        }, 5000);
    }
});