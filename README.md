Esta aplicação permite o cadastro, edição, visualização e exclusão de equipamentos utilizando Python, Django, JavaScript, HTML e APIs REST.

## 🚀 Começando

### 🌟 Principais Funcionalidades</br>
• Listar todos os equipamentos cadastrados.</br>
• Cadastrar novos equipamentos na base de dados.</br>
• Editar as informações dos equipamentos conforme necessário.</br>
• Remover equipamentos que não são mais necessários.</br>
• Visualizar informações detalhadas de qualquer equipamento.</br>

### 🗂️ Estrutura do Projeto</br>
• `equipamentos/`: App Django responsável pelo gerenciamento dos equipamentos.</br>
• `templates/`: Arquivos HTML para a interface web.</br>
• `static/`: Arquivos JavaScript, CSS e outras mídias estáticas.</br>

### 🧪 Testes</br>
Os testes automatizados podem ser executados com o seguinte comando:

```python manage.py test```

### ⚙️ Configuração do Ambiente

Siga os passos abaixo para configurar o ambiente e executar o projeto localmente:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SamuelAMT/equipamentos.git
   cd equipamentos

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows
    ```

3. Instale as dependências:
```pip install -r requirements.txt```

4. Realize as migrações do banco de dados:
```python manage.py migrate```

5. Inicie o servidor de desenvolvimento:
```python manage.py runserver```

Agora você pode acessar a aplicação em http://localhost:8000.

### 👤 Autor</br>
Samuel Miranda - [LinkedIn](https://www.linkedin.com/in/samuel-miranda-software-py/)
