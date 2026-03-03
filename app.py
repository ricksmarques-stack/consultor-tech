import streamlit as st
import pandas as pd

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Consultor Hardware Alphaville", page_icon="💻", layout="wide")

# Estilização básica para parecer um software corporativo
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SEU BANCO DE DADOS DE PRODUTOS (Edite os links e preços aqui) ---
# Dica: Substitua os links pelos seus links de afiliado ou link do catálogo do seu parceiro
produtos = [
    {
        "nome": "Lenovo ThinkPad L14 (Seminovo Premium)",
        "perfil": ["Administrativo", "RH", "Comercial", "Financeiro"],
        "cpu": "Intel Core i5", "ram": "16GB", "ssd": "256GB",
        "preco": 2900, "link": "https://wa.me/SEU_NUMERO?text=Quero+saber+do+ThinkPad+L14",
        "venda": "O padrão ouro de durabilidade corporativa. Teclado excelente para digitação pesada."
    },
    {
        "nome": "Dell Vostro 3520 (Novo)",
        "perfil": ["Administrativo", "Vendas", "Educação"],
        "cpu": "Intel Core i5 12ª Ger", "ram": "8GB", "ssd": "512GB",
        "preco": 3400, "link": "https://wa.me/SEU_NUMERO?text=Quero+saber+do+Dell+Vostro",
        "venda": "Garantia Dell On-site. Ideal para quem não pode ter a máquina parada um único dia."
    },
    {
        "nome": "MacBook Air M2 (Novo)",
        "perfil": ["Diretoria", "Marketing", "Designer", "Dev. Mobile"],
        "cpu": "Apple M2", "ram": "8GB (Integrada)", "ssd": "256GB",
        "preco": 7200, "link": "https://wa.me/SEU_NUMERO?text=Quero+saber+do+MacBook+Air",
        "venda": "Status, bateria que dura 15h e tela de altíssima fidelidade de cor."
    },
    {
        "nome": "Avell Storm (Workstation)",
        "perfil": ["Engenharia", "Arquiteto", "Editor de Vídeo", "Dev. Backend"],
        "cpu": "Intel i7 Série H", "ram": "32GB", "ssd": "1TB",
        "preco": 8900, "link": "https://wa.me/SEU_NUMERO?text=Quero+saber+do+Avell+Storm",
        "venda": "Poder de processamento bruto para renderização 3D e cálculos complexos."
    }
]

# --- 3. INTERFACE ---
st.title("💻 Diagnóstico de Hardware Corporativo")
st.subheader("Evite o desperdício. Compre a performance exata que sua equipe precisa.")

with st.sidebar:
    st.header("Filtros de Consultoria")
    cargo = st.selectbox("Qual o cargo/função do colaborador?", 
                         ["Administrativo", "Comercial", "Marketing", "Designer", "Engenharia", "Dev. Backend", "Diretoria"])
    
    budget = st.slider("Orçamento máximo (R$)", 2000, 15000, 5000, step=500)
    st.info("💡 Dica: Invista em RAM para cargos multitarefa.")

# --- 4. LÓGICA DE RECOMENDAÇÃO ---
st.markdown(f"### Recomendações para: **{cargo}** (Até R$ {budget})")

# Filtragem
rec_final = [p for p in produtos if cargo in p['perfil'] and p['preco'] <= budget]

if not rec_final:
    st.warning("⚠️ Nenhuma configuração exata encontrada para este orçamento. Tente aumentar o limite ou mudar o cargo.")
else:
    for item in rec_final:
        with st.expander(f"⭐ {item['nome']} - R$ {item['preco']}", expanded=True):
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                st.write(f"**Processador:** {item['cpu']}")
                st.write(f"**Memória:** {item['ram']}")
                st.write(f"**Armazenamento:** {item['ssd']}")
            with col2:
                st.write("**Por que esta máquina?**")
                st.write(f"_{item['venda']}_")
            with col3:
                st.link_button("Solicitar Cotação (WhatsApp)", item['link'])

st.divider()
st.caption("Alphaville Tech Consulting - Dimensionando sua produtividade.")
