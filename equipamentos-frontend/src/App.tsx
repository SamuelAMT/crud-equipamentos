import React from 'react';
import EquipamentoForm, { EquipamentoFormData } from './components/EquipamentoForm';

const App: React.FC = () => {
  const handleFormSubmit = async (data: EquipamentoFormData) => {
    try {
      const response = await fetch('http://localhost:8000/api/equipamentos/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      
      if (response.ok) {
        console.log('Equipamento cadastrado com sucesso!');
      } else {
        console.error('Erro ao cadastrar o equipamento.');
      }
    } catch (error) {
      console.error('Erro na requisição:', error);
    }
  };

  return (
    <div>
      <h1>Cadastro de Equipamentos</h1>
      <EquipamentoForm onSubmit={handleFormSubmit} />
    </div>
  );
};

export default App;