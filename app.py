import streamlit as st
import os
from rag_engine import RAGEngine, get_groq_api_key

st.set_page_config(
    page_title="Nexus Bank - Agente Corporativo",
    page_icon="🏦",
    layout="wide"
)

# Estilização Nexus Bank
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stApp header { background-color: rgba(0,0,0,0); }
    h1 { color: #00d2ff; }
    </style>
""", unsafe_allow_html=True)

st.title("🏦 Nexus Bank - Base de Conhecimento Interna")
st.caption("Agente Inteligente de Atendimento ao Colaborador | Powered by Groq & RAG")

# Validação da API Key
groq_api_key = get_groq_api_key()

if not groq_api_key:
    groq_api_key = st.sidebar.text_input("Insira sua Groq API Key:", type="password")

if not groq_api_key:
    st.warning("⚠️ Insira a variável GROQ_API_KEY no arquivo .env, nos Secrets do Streamlit ou na barra lateral.")
    st.stop()

# Inicialização do Engine RAG (carregamento automático da pasta /docs)
@st.cache_resource(show_spinner="Carregando documentos da pasta /docs...")
def init_rag():
    return RAGEngine()

rag_engine = init_rag()

# Exibição dos documentos carregados na barra lateral
st.sidebar.title("📚 Documentos Carregados")
if rag_engine.documents:
    sources_summary = set(doc.metadata.get("source") for doc in rag_engine.documents)
    for src in sources_summary:
        st.sidebar.markdown(f"- 📄 `{src}`")
else:
    st.sidebar.error("Nenhum documento encontrado na pasta `docs/`!")

# Histórico de Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Faça uma pergunta sobre processos ou regras do Nexus Bank..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Consultando diretrizes do Nexus Bank..."):
            try:
                response_text, sources = rag_engine.query(prompt, groq_api_key)
                st.markdown(response_text)

                if sources:
                    st.caption(f"📌 **Fontes Consultadas:** {', '.join(sources)}")

                st.session_state.messages.append({"role": "assistant", "content": response_text})
            except Exception as e:
                st.error(f"Erro no processamento da requisição: {e}")