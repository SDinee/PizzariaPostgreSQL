const entrega = document.getElementById('entrega');
const pagamento = document.getElementById('pagamento');
const finalizar = document.getElementById('finalizar');

function validar() {
    if (entrega.value !== "" && pagamento.value !== "") {
        finalizar.disabled = false; // habilita
    } else {
        finalizar.disabled = true;  // desabilita
    }
}

entrega.addEventListener('change', validar);
pagamento.addEventListener('change', validar);