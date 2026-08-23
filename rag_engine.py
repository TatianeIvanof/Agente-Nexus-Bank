import os
from dotenv import load_dotenv
from groq import Groq
from document_processor import load_documents_from_folder, split_documents

load_dotenv()

def get_groq_api_key():
    # Tenta buscar das variáveis de ambiente ou dos secrets do Streamlit
    try:
        import streamlit as st
        if "GROQ_API_KEY" in st.secrets:
            return st.secrets["GROQ_API_KEY"]
    except Exception:
        pass
    return os.getenv("GROQ_API_KEY", "")

class RAGEngine:
    def __init__(self):
        self.documents = load_documents_from_folder("docs")
        self.chunks = split_documents(self.documents)

    def search_context(self, query, top_k=5):
        """Busca por relevância textual simples nos chunks do contexto."""
        if not self.chunks:
            return "", []

        query_words = set(query.lower().split())
        scored_chunks = []

        for chunk in self.chunks:
            content_lower = chunk.page_content.lower()
            score = sum(1 for word in query_words if word in content_lower)
            if score > 0:
                scored_chunks.append((score, chunk))

        scored_chunks.sort(key=lambda x: x[0], reverse=True)
        selected_chunks = [item[1] for item in scored_chunks[:top_k]]

        if not selected_chunks:
            selected_chunks = self.chunks[:top_k]

        context_text = ""
        sources = set()

        for chunk in selected_chunks:
            src = chunk.metadata.get("source", "Desconhecido")
            sources.add(src)
            context_text += f"\n--- FONTE: {src} ---\n{chunk.page_content}\n"

        return context_text, list(sources)

    def query(self, prompt, api_key):
        client = Groq(api_key=api_key)
        context, sources = self.search_context(prompt)

        system_prompt = (
            "Você é o Agente de Inteligência Artificial Corporativo do Nexus Bank.\n"
            "Sua missão é responder dúvidas dos colaboradores com precisão, educação e tom profissional.\n\n"
            "REGRAS DE RESPOSTA:\n"
            "1. Responda ESTRITAMENTE com base no contexto fornecido abaixo.\n"
            "2. Se a resposta não estiver clara no contexto, responda EXATAMENTE:\n"
            "'Não encontrei essa informação nos documentos internos do Nexus Bank. Por favor, consulte o departamento responsável (RH, TI, Financeiro ou Jurídico).'\n"
            "3. Cite sempre os documentos originais utilizados.\n\n"
            f"--- CONTEXTO RELEVANTE DOS DOCUMENTOS DA EMPRESA ---\n{context[:20000]}"
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            model="openai/gpt-oss-120b",
            temperature=0.1
        )

        response_text = chat_completion.choices[0].message.content
        return response_text, sources