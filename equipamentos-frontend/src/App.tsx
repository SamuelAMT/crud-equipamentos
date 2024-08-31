import React from 'react';
import EquipamentoForm, { EquipamentoFormData } from './components/EquipamentoForm';
import Header from './components/Header';
import styles from './styles/equipamentos_form.module.css';

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
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      console.log('Equipamento cadastrado com sucesso!');
    } catch (error) {
      console.error('Erro na requisição:', error);
    }
  };

  return (
    <div className={styles["app-container"]}>
      <Header />
      <div className={styles["form-container"]}>
        <EquipamentoForm onSubmit={handleFormSubmit} />
      </div>
    </div>
  );
};

export default App;