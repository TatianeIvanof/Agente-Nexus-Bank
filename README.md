# 🏦 Nexus Bank — Agente Corporativo de IA

O **Nexus Bank – Agente Corporativo** é uma solução de inteligência artificial desenvolvida para atuar como uma base de conhecimento conversacional centralizada, de acesso universal a todos os colaboradores da empresa.

O agente utiliza a arquitetura **RAG (Retrieval-Augmented Generation)** com suporte à **API Groq** para interpretar, consultar e responder dúvidas com base em múltiplos documentos internos, incluindo **PDF, DOCX, XLSX, PPTX, CSV, MD, JSON e HTML**.

A solução foi projetada para fornecer respostas fundamentadas nos documentos disponíveis, reduzindo o risco de alucinações e apresentando as respectivas fontes utilizadas na resposta.

---

## 🏛️ Cenário e Objetivo

No contexto do **Nexus Bank**, documentos regulatórios, manuais operacionais, políticas de governança, diretrizes de RH e tabelas de tarifas encontram-se distribuídos em diversos formatos.

O objetivo deste projeto é disponibilizar uma interface amigável e acessível aos colaboradores, capaz de responder perguntas operacionais, regulatórias e corporativas de forma rápida e centralizada.

### Objetivos principais

* Centralizar o conhecimento corporativo.
* Facilitar o acesso às informações internas.
* Reduzir o tempo gasto na busca por documentos.
* Apoiar colaboradores na consulta de políticas e procedimentos.
* Fornecer respostas baseadas em fontes documentais.
* Reduzir respostas sem fundamentação documental.
* Apresentar as fontes utilizadas pelo agente.
* Permitir uma arquitetura escalável para inclusão de novos documentos.

---

## 📐 Arquitetura da Solução

O fluxo de processamento de dados e geração das respostas segue a pipeline abaixo:

```text
┌─────────────────────────────────────────────────────────┐
│               Documentos Internos (/docs)               │
│       PDF, DOCX, XLSX, PPTX, CSV, MD, JSON, HTML        │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│              Extração e Limpeza por Formato             │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│            Chunking Adaptativo + Metadados              │
│       Divisão de texto + overlap + fonte/página         │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│          Engine de Recuperação e Busca Semântica        │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│     Prompt do Sistema + Contexto Recuperado (RAG)       │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│       Groq API — LLaMA 3.3 70B Versatile                │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│      Resposta Estruturada + Fontes / Fallback            │
└─────────────────────────────────────────────────────────┘
```

### Funcionamento do RAG

O agente não depende exclusivamente do conhecimento prévio do modelo de linguagem.

Quando uma pergunta é realizada:

1. O sistema recebe a pergunta do usuário.
2. Os documentos internos são consultados.
3. Os conteúdos mais relevantes são recuperados.
4. Os trechos encontrados são enviados como contexto para o modelo.
5. O modelo gera a resposta utilizando o contexto recuperado.
6. A resposta apresenta as fontes utilizadas.
7. Caso não exista informação suficiente nos documentos, o agente utiliza um mecanismo de **fallback**, informando que a informação não foi encontrada.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia                  | Finalidade                             |
| --------------------------- | -------------------------------------- |
| **Python 3.10+**            | Linguagem principal                    |
| **Streamlit**               | Interface web                          |
| **Groq API**                | Inferência do modelo de linguagem      |
| **LLaMA 3.3 70B Versatile** | Modelo de linguagem                    |
| **pypdf**                   | Processamento de PDFs                  |
| **python-docx**             | Processamento de documentos DOCX       |
| **python-pptx**             | Processamento de apresentações PPTX    |
| **pandas**                  | Manipulação de dados                   |
| **openpyxl**                | Processamento de arquivos XLSX         |
| **BeautifulSoup4**          | Processamento de HTML                  |
| **python-dotenv**           | Gerenciamento de variáveis de ambiente |
| **Streamlit Cloud**         | Hospedagem e deploy                    |

### Principais componentes

* **Document Processor:** responsável pela leitura, extração, limpeza e divisão dos documentos.
* **RAG Engine:** responsável pela recuperação de informações e integração com o modelo de linguagem.
* **Streamlit App:** responsável pela interface de interação com o usuário.
* **Groq API:** responsável pela geração das respostas utilizando o modelo LLaMA.

---

## 📂 Estrutura do Projeto

```text
nexus-bank-agent/
│
├── .env                  # Variáveis de ambiente (NÃO COMMITAR)
├── .gitignore            # Arquivos ignorados pelo Git
├── app.py                # Interface principal em Streamlit
├── document_processor.py # Leitura, extração e chunking dos documentos
├── rag_engine.py         # Engine RAG e integração com Groq
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação do projeto
│
└── docs/                 # Documentos internos utilizados pelo agente
    ├── Política de Privacidade e Proteção de Dados (LGPD).pdf
    ├── Termos e Condições de Uso da Conta Digital.pdf
    ├── Perguntas Frequentes (FAQ) - Transações e Limites.pdf
    ├── Política de Segurança e Prevenção a Fraudes.pdf
    ├── Tabela de Tarifas e Comissões do Serviço.pdf
    ├── Política de PLD/FTP.pdf
    ├── Política de KYC (Know Your Customer).pdf
    ├── Política de KYP e KYE (Know Your Partner & Employee).pdf
    ├── Política de Uso de Nuvem e Terceirização.pdf
    ├── Código de Ética e Conduta.pdf
    ├── Política de Gerenciamento de Riscos Integrados (GIR).pdf
    ├── Política de Prevenção a Conflitos de Interesses.pdf
    ├── Política de Brindes, Hospitalidades e Anticorrupção.pdf
    ├── Política de Relacionamento com o Cliente.pdf
    ├── Política de Cobrança de Tarifas.pdf
    ├── Política de Brindes, Hospitalidades e Anticorrupção.pdf
    ├── Política de Transparência Fiscal (e-Financeira).pdf
    ├── Política de Gestão de Pessoas e RH.pdf
```

---

## 🔐 Segurança

A chave da API Groq **não deve ser armazenada diretamente no código-fonte nem publicada no GitHub**.

Utilize um arquivo `.env` local:

```env
GROQ_API_KEY=gsk_sua_chave_groq_aqui
```

O arquivo `.env` deve estar incluído no `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

### Boas práticas

* Nunca publicar chaves de API no Git.
* Nunca inserir credenciais diretamente no código.
* Não utilizar informações corporativas reais em repositórios públicos.
* Controlar o acesso aos documentos internos.
* Utilizar variáveis de ambiente para informações sensíveis.
* Revisar permissões do repositório antes do deploy.
* Evitar o envio de dados pessoais ou confidenciais para serviços externos sem autorização corporativa.

---

## ⚙️ Instalação e Execução Local

### 1. Clonar o repositório

```bash
git clone https://github.com/TatianeIvanof/nexus-bank-agent.git

cd nexus-bank-agent
```

### 2. Criar o ambiente virtual

#### Windows PowerShell

```powershell
python -m venv venv

.\venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar a API Groq

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=gsk_sua_chave_groq_aqui
```

> **Importante:** não compartilhe sua chave de API e não faça commit do arquivo `.env`.

### 5. Adicionar os documentos

Coloque os documentos corporativos na pasta:

```text
docs/
```

Formatos suportados:

```text
PDF
DOCX
XLSX
PPTX
CSV
MD
JSON
HTML
```

### 6. Executar a aplicação

```bash
streamlit run app.py
```

Após a inicialização, o Streamlit disponibilizará a aplicação localmente.

---

## 💬 Exemplos de Utilização

### Exemplo 1 — Operações e Transações

**Pergunta:**

> Qual é o limite operacional e o horário estipulado para o Pix noturno?

**Resposta esperada:**

> O Pix noturno tem limite padrão de R$ 1.000,00 por período, conforme a regulamentação do Banco Central, e pode ser utilizado no horário das 20:00 às 06:00.

📌 **Fonte consultada:** `Nexus_Bank_FAQ_Transacoes_e_Limites.pdf – seção “Pix Noturno (20:00 às 06:00)”.`

![Demonstração Resposta Operações e Transações da Nexus Bank Agent](docs/screenshot1.png)

---

### Exemplo 2 — Compliance e Governança

**Pergunta:**

> Qual é o valor máximo permitido para o recebimento de brindes ou hospitalidades por colaboradores?

**Resposta esperada:**

> O valor máximo permitido para o recebimento de brindes ou hospitalidades pelos colaboradores é R$ 500,00 (para presentes de relacionamento comercial), sendo necessária aprovação prévia.

📌 **Fonte consultada:** `Nexus_Bank_Politica_Anticorrupcao_Brindes.pdf – tabela “Item – Valor Limite Permitido – Aprovação Exigida”.`

![Demonstração Resposta Compliance e Governança da Nexus Bank Agent](docs/screenshot2.png)

---

### Exemplo 3 — Controle de Alucinação / Fallback

**Pergunta:**

> Qual é a previsão de inflação para o ano que vem?

**Resposta esperada:**

> Não encontrei essa informação nos documentos internos do Nexus Bank. Por favor, consulte o departamento responsável (RH, TI, Financeiro ou Jurídico).

![Demonstração Resposta Compliance e Governança da Nexus Bank Agent](docs/screenshot3.png)

Esse mecanismo evita que o agente apresente como fato uma informação que não esteja disponível na base documental.

---

## 🧠 Estratégia de Controle de Alucinação

O Nexus Bank foi estruturado para priorizar informações presentes nos documentos disponibilizados.

A lógica esperada é:

```text
Pergunta do usuário
        │
        ▼
Busca na base documental
        │
        ▼
Encontrou informação relevante?
      /     \
    SIM      NÃO
     │        │
     ▼        ▼
Gera resposta  Fallback
com fonte      informativo
     │
     ▼
Apresenta resposta
```

Quando não houver evidência documental suficiente, o agente deve evitar criar informações e informar ao usuário que a resposta não foi localizada na base disponível.

---

## 📊 Fluxo de Consulta

```text
                    USUÁRIO
                       │
                       ▼
                Faz uma pergunta
                       │
                       ▼
              ┌─────────────────┐
              │  RAG Engine     │
              └────────┬────────┘
                       │
                       ▼
             Busca informações
              nos documentos
                       │
                       ▼
              Recupera contexto
                       │
                       ▼
             ┌─────────────────┐
             │    Groq API     │
             │ LLaMA 3.3 70B   │
             └────────┬────────┘
                       │
                       ▼
              Resposta baseada
               no contexto
                       │
                       ▼
             Fonte apresentada
                       │
                       ▼
                    USUÁRIO
```

---

## 📸 Demonstração da Aplicação

Adicione aqui uma imagem ou GIF demonstrando a execução da aplicação:

```text
docs/
└── screenshot.png
```
![Demonstração do Nexus Bank Agent](docs/screenshot0.png)

Exemplo para inserir uma imagem no README:

```markdown
![Demonstração do Nexus Bank Agent](docs/screenshot.png)
```
![Demonstração de perguntas e Respostas da apliacação](docs/Nexus Bank - Agente Corporativo · Streamlit.pdf)
---

## ☁️ Deploy na Streamlit Cloud

O projeto pode ser publicado na nuvem utilizando o **Streamlit Cloud**.

Fluxo recomendado:

```text
GitHub
   │
   ▼
Repositório Nexus Bank Agent
   │
   ▼
Streamlit Cloud
   │
   ├── Configuração dos Secrets
   │
   ├── Instalação do requirements.txt
   │
   └── Execução do app.py
```

### Configuração da chave

No ambiente de deploy, configure a variável:

```text
GROQ_API_KEY
```

A chave deve ser configurada como **Secret**, e não diretamente no código-fonte.

---

## 🔗 Aplicação em Nuvem

**Link de acesso:**

https://nexus-bank-agent.streamlit.app

> **Observação:** substitua o endereço acima pelo endereço real da aplicação após realizar o deploy.

---

## 🚀 Possíveis Evoluções

O projeto pode evoluir para uma arquitetura corporativa mais completa, incluindo:

* [ ] Banco vetorial para armazenamento dos embeddings.
* [ ] Controle de acesso por perfil de usuário.
* [ ] Autenticação corporativa.
* [ ] Integração com Microsoft Entra ID / SSO.
* [ ] Registro e auditoria das perguntas realizadas.
* [ ] Monitoramento de utilização do agente.
* [ ] Avaliação automática da qualidade das respostas.
* [ ] Versionamento dos documentos.
* [ ] Controle de validade dos documentos.
* [ ] Dashboard de utilização.
* [ ] Classificação automática dos documentos.
* [ ] Integração com SharePoint.
* [ ] Integração com sistemas corporativos.
* [ ] Mecanismo de feedback das respostas.
* [ ] Gestão de permissões por área.
* [ ] Criptografia e controles adicionais de segurança.

---

## 📌 Benefícios Esperados

### Para os colaboradores

* Acesso rápido ao conhecimento corporativo.
* Redução do tempo de pesquisa.
* Interface simples e conversacional.
* Consulta centralizada de documentos.

### Para a organização

* Maior disseminação do conhecimento.
* Padronização das informações.
* Redução de consultas repetitivas às áreas especialistas.
* Maior eficiência operacional.
* Apoio à governança e compliance.
* Melhoria da experiência dos colaboradores.

---

## ⚠️ Aviso Importante

O Nexus Bank Agent é uma ferramenta de apoio à consulta de informações em uma empresa fictícia.

---

## 📄 Licença

Este projeto é destinado a fins **educacionais, demonstrativos e/ou corporativos**, conforme as regras de utilização definidas pelo proprietário do repositório.

---

## 👩‍💻 Autor

**Tatiane Ivanof**

Projeto desenvolvido como solução de aplicação de **Inteligência Artificial Generativa, RAG, Gestão do Conhecimento e automação corporativa**.
