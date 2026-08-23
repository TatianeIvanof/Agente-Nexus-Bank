# 🏦 Nexus Bank - Agente de Inteligência Artificial Corporativo

Agente virtual de suporte interno desenvolvido para os colaboradores do **Nexus Bank**. A solução utiliza a arquitetura **RAG (Retrieval-Augmented Generation)** integrada à **API Groq** para ler, processar e responder dúvidas com base em documentações internas.

---

## 📐 Arquitetura da Solução

```text
[ Documentos Internos (/docs) ] 
       │ (PDF, DOCX, XLSX, PPTX, CSV, MD, JSON, HTML)
       ▼
[ Extrator & Limpeza de Texto ]
       │
       ▼
[ Divisão em Chunks + Metadados ]
       │
       ▼
[ Mecanismo de Busca / Recuperação ]
       │
       ▼
[ Prompt do Sistema + Contexto ] ──► [ Groq API (LLaMA-3.3-70B) ]
                                                │
                                                ▼
                                    [ Resposta com Citações ]

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.10+

Interface Web: Streamlit

LLM Engine: Groq API (llama-3.3-70b-versatile)

Processamento de Documentos: PyPDF, python-docx, pandas, openpyxl, python-pptx, BeautifulSoup4

Hospedagem: Streamlit Cloud

🚀 Como Executar o Projeto Localmente
Clone o repositório:

Bash
git clone [https://github.com/SEU_USUARIO/nexus-bank-agent.git](https://github.com/SEU_USUARIO/nexus-bank-agent.git)
cd nexus-bank-agent
Crie um ambiente virtual e ative-o:

Bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
Instale as dependências:

Bash
pip install -r requirements.txt
Configure a Chave da API:
Crie um arquivo .env na raiz do projeto com o conteúdo:

Snippet de código
GROQ_API_KEY=gsk_sua_chave_groq_aqui
Adicione os documentos:
Insira os arquivos da empresa dentro da pasta /docs.

Inicie a aplicação:

Bash
streamlit run app.py
❓ Exemplos de Uso
Pergunta 1:
"Qual é a política de reembolso para viagens de trabalho no Nexus Bank?"

Resposta Gerada:

De acordo com a Política de Viagens (v2.1), o reembolso de refeições é de até R$ 120,00 por dia mediante apresentação de nota fiscal até 5 dias úteis após o retorno.

📌 Fontes Consultadas: politica_viagens.pdf

Pergunta 2:
"Quem ganha a copa do mundo de futebol em 2030?"

Resposta Gerada:

Não encontrei essa informação nos documentos internos do Nexus Bank. Por favor, consulte o departamento responsável (RH, TI, Financeiro ou Jurídico).

📸 Demonstração em Nuvem
(Insira aqui um GIF, imagem ou link do vídeo demonstrando o agente rodando no Streamlit Cloud)

🔗 Link da Aplicação Rodando em Nuvem: https://nexus-bank-agent.streamlit.app