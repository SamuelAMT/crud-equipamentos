import React, { useState } from 'react';
import styles from '../styles/equipamentos_form.module.css';

interface EquipamentoFormProps {
  onSubmit: (data: EquipamentoFormData) => void;
}

export interface EquipamentoFormData {
  nome: string;
  descricao?: string;
  status: string;
  tipo: string;
  fabricante: string;
  modelo: string;
  numero_serie: string;
  data_compra: string;
  valor_compra: number;
  data_ultima_manutencao?: string;
  data_proxima_manutencao?: string;
}

const EquipamentoForm: React.FC<EquipamentoFormProps> = ({ onSubmit }) => {
  const [formData, setFormData] = useState<EquipamentoFormData>({
    nome: '',
    descricao: '',
    status: 'em_estoque',
    tipo: '',
    fabricante: '',
    modelo: '',
    numero_serie: '',
    data_compra: '',
    valor_compra: 0,
    data_ultima_manutencao: '',
    data_proxima_manutencao: '',
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <div className={styles["form-container"]}>
      <h2 className={styles["form-title"]}>Cadastro de Equipamentos</h2>
      <form onSubmit={handleSubmit} className={styles["equipamento-form"]}>
        <div className={styles["form-group"]}>
          <label className={styles["label"]}>Nome:</label>
          <input
            type="text"
            name="nome"
            value={formData.nome}
            onChange={handleChange}
            required
            className={styles["input"]}
          />
        </div>
        <div className={styles["form-group"]}>
          <label className={styles["label"]}>Descrição:</label>
          <textarea
            name="descricao"
            value={formData.descricao}
            onChange={handleChange}
            className={styles["textarea"]}
          />
        </div>
        <div className={styles["form-group"]}>
          <label className={styles["label"]}>Status:</label>
          <select
            name="status"
            value={formData.status}
            onChange={handleChange}
            required
            className={styles["select"]}
          >
            <option value="em_uso">Em Uso</option>
            <option value="em_estoque">Em Estoque</option>
            <option value="manutencao">Em Manutenção</option>
            <option value="nao_funcional">Não Funcional</option>
          </select>
        </div>
        <div className={styles["form-group"]}>
          <label className={styles["label"]}>Tipo:</label>
          <input
            type="text"
            name="tipo"
            value={formData.tipo}
            onChange={handleChange}
            required
            className={styles["input"]}
          />
        </div>
        <div className={styles["form-group"]}>
          <label className={styles["label"]}>Fabricante:</label>
          <input
            type="text"
            name="fabricante"
            value={formData.fabricante}
            onChange={handleChange}
            required
            className={styles["input"]}
          />
        </div>
        <div className={styles["form-group"]}>
          <label className={styles["label"]}>Modelo:</label>
          <input
            type="text"
            name="modelo"
            value={formData.modelo}
            onChange={handleChange}
            required
            className={styles["input"]}
          />
        </div>
        <div className={styles["form-group"]}>
          <label className={styles["label"]}>Número de Série:</label>
          <input
            type="text"
            name="numero_serie"
            value={formData.numero_serie}
            onChange={handleChange}
            required
            className={styles["input"]}
          />
        </div>
        <div className={styles["form-group"]}>
          <label className={styles["label"]}>Data de Compra:</label>
          <input
            type="date"
            name="data_compra"
            value={formData.data_compra}
            onChange={handleChange}
            required
            className={styles["input"]}
          />
        </div>
        <div className={styles["form-group"]}>
          <label className={styles["label"]}>Valor de Compra:</label>
          <input
            type="number"
            name="valor_compra"
            value={formData.valor_compra}
            onChange={handleChange}
            required
            className={styles["input"]}
          />
        </div>
        <div className={styles["form-group"]}>
          <label className={styles["label"]}>Data da Última Manutenção:</label>
          <input
            type="date"
            name="data_ultima_manutencao"
            value={formData.data_ultima_manutencao}
            onChange={handleChange}
            className={styles["input"]}
          />
        </div>
        <div className={styles["form-group"]}>
          <label className={styles["label"]}>Data da Próxima Manutenção:</label>
          <input
            type="date"
            name="data_proxima_manutencao"
            value={formData.data_proxima_manutencao}
            onChange={handleChange}
            className={styles["input"]}
          />
        </div>
        <button type="submit" className={styles["submit-button"]}>Cadastrar Equipamento</button>
      </form>
    </div>
  );
};

export default EquipamentoForm;