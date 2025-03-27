# Sistema de Consulta de Operadoras de Saúde

Este projeto é um sistema web para consulta de operadoras de planos de saúde registradas na ANS (Agência Nacional de Saúde Suplementar). O sistema permite buscar informações detalhadas sobre operadoras através de diferentes critérios como nome, CNPJ, registro ANS ou localização.

## 🚀 Tecnologias Utilizadas

### Backend
- Python 3.8+
- FastAPI
- Pandas
- Uvicorn
- Python-dotenv

### Frontend
- Vue.js 3
- Vue Router
- Axios
- Font Awesome
- Vite

## 📁 Estrutura do Projeto

```
.
├── api/
│   ├── backend/
│   │   ├── main.py              # API FastAPI
│   │   ├── requirements.txt     # Dependências Python
│   │   └── ...
│   └── frontend/
│       └── front-intuitive/
│           ├── src/
│           │   ├── components/  # Componentes Vue
│           │   ├── views/       # Páginas
│           │   └── router/      # Configuração de rotas
│           └── ...
```

## 🛠️ Instalação e Configuração

### Backend

1. Navegue até a pasta do backend:
```bash
cd backend
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Inicie o servidor:
```bash
uvicorn main:app --reload --port 8001
```

### Frontend

1. Navegue até a pasta do frontend:
```bash
cd frontend/front-intuitive
```

2. Instale as dependências:
```bash
npm install
```

3. Inicie o servidor de desenvolvimento:
```bash
npm run dev
```

## 🌐 Acessando o Sistema

- Frontend: http://localhost:5173
- Backend: http://localhost:8001
- API Docs: http://localhost:8001/docs

## 🔍 Funcionalidades

### Busca de Operadoras
- Pesquisa por nome da operadora
- Pesquisa por CNPJ
- Pesquisa por registro ANS
- Pesquisa por localização

### Informações Disponíveis
- Nome fantasia
- Razão social
- Registro ANS
- CNPJ
- Modalidade
- Cidade/UF

### Interface
- Design responsivo
- Feedback visual de carregamento
- Tratamento de erros
- Layout moderno e intuitivo

## 🔒 Requisitos do Sistema

### Backend
- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)
- Acesso à internet para instalação de dependências

### Frontend
- Node.js 14 ou superior
- NPM ou Yarn
- Navegador web moderno

## 📝 Notas de Desenvolvimento

### Backend
- API RESTful desenvolvida com FastAPI
- Processamento eficiente de dados com Pandas
- CORS configurado para desenvolvimento local
- Tratamento de caracteres especiais nas buscas

### Frontend
- Componentização com Vue.js 3
- Gerenciamento de estado com Composition API
- Roteamento com Vue Router
- Requisições HTTP com Axios
- Estilização com CSS moderno

## 🤝 Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- Desenvolvido por [Seu Nome]

## 📞 Suporte

Para suporte, envie um email para [seu-email@exemplo.com] 