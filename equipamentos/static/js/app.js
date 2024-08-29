document.addEventListener('DOMContentLoaded', function() {
    fetchEquipamento();
});

function fetchEquipamento() {
    fetch('/api/equipamentos/')
        .then(response => response.json())
        .then(data => {
            let list = document.getElementById('equipamento-list');
            list.innerHTML = '';
            data.forEach(equipamento => {
                let item = document.createElement('div');
                item.innerHTML = `${equipamento.name} - ${equipamento.description}`;
                list.appendChild(item);
            });
        });
}

function addEquipamento() {
    const equipamento = {
        id: 1,
        nome: 'Equipamento braço articulado',
        descricao: 'Equipamento para movimentação de cargas',
        status: 'em_estoque',
        tipo: 'Mecânico',
        fabricante: 'Tesla Inc.',
        modelo: 'Model X',
        numero_serie: '123456789',
        data_compra: '2024-08-29',
        valor_compra: '150000.00',
        data_ultima_manutencao: '2024-08-10',
        data_proxima_manutencao: '2025-08-10'
    }

    fetch('/api/equipamentos/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(equipamento)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        fetchEquipamento();
    });
}
