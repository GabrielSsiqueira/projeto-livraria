// Seu JavaScript
function incrementarQuantidade(button) {
    var spanQuantidade = button.parentNode.querySelector('.quantidade');
    var quantidade = parseInt(spanQuantidade.textContent);

    quantidade++;
    spanQuantidade.textContent = quantidade;
}

function decrementarQuantidade(button) {
    var spanQuantidade = button.parentNode.querySelector('.quantidade');
    var quantidade = parseInt(spanQuantidade.textContent);

    if (quantidade > 1) {
        quantidade--;
        spanQuantidade.textContent = quantidade;
    }
}

document.addEventListener('DOMContentLoaded', function () {
    var removeButtons = document.querySelectorAll('.remove');
    removeButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            removerItem(button);
        });
    });

    function removerItem(button) {
        // Adicione aqui a lógica para remover o item do carrinho
        var row = button.closest('tr');
        row.remove();
        // Atualize o carrinho e valores totais
        updateCartDisplay();
    }

    function updateCartDisplay() {
        // Adicione aqui a lógica para atualizar a exibição do carrinho
        console.log('Carrinho atualizado:', cartItems);
    }

    // Restante do seu código JavaScript
});

document.addEventListener('DOMContentLoaded', function () {
    // ... (código existente)

    var buttonFinalizarCompra = document.getElementById('button-finalizar');
    buttonFinalizarCompra.addEventListener('click', function () {
        finalizarCompra();
    });

    function finalizarCompra() {
        // Exibe um alerta de compra realizada com sucesso
        alert('Compra realizada com sucesso! Até a próxima!');

    }

});
// Seu JavaScript
function incrementarQuantidade(button) {
    var spanQuantidade = button.parentNode.querySelector('.quantidade');
    var quantidade = parseInt(spanQuantidade.textContent);
    var precoUnitario = extrairPrecoUnitario(button);

    quantidade++;
    spanQuantidade.textContent = quantidade;

    atualizarSubtotal(button, quantidade * precoUnitario);
    atualizarTotal();
}

function decrementarQuantidade(button) {
    var spanQuantidade = button.parentNode.querySelector('.quantidade');
    var quantidade = parseInt(spanQuantidade.textContent);
    var precoUnitario = extrairPrecoUnitario(button);

    if (quantidade > 1) {
        quantidade--;
        spanQuantidade.textContent = quantidade;

        atualizarSubtotal(button, quantidade * precoUnitario);
        atualizarTotal();
    }
}

function extrairPrecoUnitario(button) {
    var precoString = button.closest('tr').querySelector('#preco').textContent;
    return parseFloat(precoString.replace('R$', ''));
}

function atualizarSubtotal(button, novoSubtotal) {
    button.closest('tr').querySelector('.subtotal').textContent = 'R$' + novoSubtotal.toFixed(2);
}

function atualizarTotal() {
    var subtotals = document.querySelectorAll('.subtotal');
    var total = 0;

    subtotals.forEach(function (subtotal) {
        total += parseFloat(subtotal.textContent.replace('R$', ''));
    });

    document.getElementById('total').textContent = 'R$' + total.toFixed(2);
}
function atualizarResumoCompra() {
    var subtotals = document.querySelectorAll('.subtotal');
    var total = 0;

    subtotals.forEach(function (subtotal) {
        total += parseFloat(subtotal.textContent.replace('R$', ''));
    });

    var subtotalElement = document.getElementById('sub-total');
    var totalElement = document.getElementById('total');

    subtotalElement.textContent = 'R$' + total.toFixed(2);
    totalElement.textContent = 'R$' + total.toFixed(2);
}
function atualizarSubtotal(button, novoSubtotal) {
    var row = button.closest('tr');
    var subtotalElement = row.querySelector('.subtotal');
    subtotalElement.textContent = 'R$' + novoSubtotal.toFixed(2);

    atualizarResumoCompra();  // Adiciona esta linha para atualizar o resumo
}

function atualizarTotal() {
    var subtotals = document.querySelectorAll('.subtotal');
    var total = 0;

    subtotals.forEach(function (subtotal) {
        total += parseFloat(subtotal.textContent.replace('R$', ''));
    });

    var totalElement = document.getElementById('total');
    totalElement.textContent = 'R$' + total.toFixed(2);

    atualizarResumoCompra();  // Adiciona esta linha para atualizar o resumo
}

function atualizarResumoCompra() {
    var subtotals = document.querySelectorAll('.subtotal');
    var total = 0;

    subtotals.forEach(function (subtotal) {
        total += parseFloat(subtotal.textContent.replace('R$', ''));
    });

    var subtotalElement = document.getElementById('sub-total');
    var totalElement = document.getElementById('resumo');
    var footerTotalElement = document.getElementById('subtotal');

    subtotalElement.textContent = 'R$' + total.toFixed(2);
    totalElement.textContent = 'R$' + total.toFixed(2);
    footerTotalElement.textContent = 'R$' + total.toFixed(2);
}