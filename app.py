import streamlit as st
import time
from datetime import date

# --- CONFIGURAÇÃO DA PÁGINA E TEMA ---
st.set_page_config(
    page_title="Orisun - Análise de Fontes",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Simulando o CSS do "Dark Mode Acadêmico" (Roxo Profundo e Bege)
st.markdown("""
    <style>
    .stApp {
        background-color: #0F0C29;
        color: #F0EBD8;
    }
    .stSidebar {
        background-color: #1a1638;
    }
    /* Ajustes para inputs ficarem legíveis no fundo escuro */
    .stTextInput, .stSelectbox, .stDateInput, .stTextArea {
        color: #FFFFFF;
    }
    h1, h2, h3 {
        color: #F0EBD8 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL ---
with st.sidebar:
    # Placeholder para logo
    st.image("https://placeholder.com/wp-content/uploads/2018/10/placeholder.com-logo1.png", caption="ORISUN", width=150)
    st.markdown("---")
    menu_option = st.radio(
        "Navegação",
        ["Dashboard", "Registro de Fontes", "Análise Inteligente (IA)", "Catálogo", "Configurações"],
        label_visibility="collapsed"
    )

# --- PÁGINA: DASHBOARD ---
if menu_option == "Dashboard":
    st.markdown("### Home > Dashboard") # Breadcrumbs
    st.title("Dashboard")
    
    # Métricas
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de Documentos", "124")
    col2.metric("Favoritos", "12")
    col3.metric("Em Análise", "5")
    col4.metric("Pesquisadores", "3")
    
    st.markdown("---")
    st.subheader("Atividades Recentes")
    # Tabela simples simulando registros recentes
    st.dataframe([
        {"Título": "Carta de Alforria 1889", "Data": "1889-05-12", "Tipo": "Manuscrito"},
        {"Título": "Foto do Porto de Salvador", "Data": "1920", "Tipo": "Fotografia"},
        {"Título": "Diário de Bordo", "Data": "1750", "Tipo": "Diário Pessoal"},
    ], use_container_width=True)

# --- PÁGINA: REGISTRO DE FONTES ---
elif menu_option == "Registro de Fontes":
    st.markdown("### Home > Registro de Fontes")
    st.title("Cadastro Manual de Fonte")
    
    with st.form("registro_form"):
        # Seção 1: Identificação
        st.subheader("1. Identificação Básica")
        c1, c2 = st.columns(2)
        titulo = c1.text_input("Título do Documento *")
        titulo_orig = c2.text_input("Título Original")
        autor = c1.text_input("Criador/Autor")
        local = c2.text_input("Localização de Origem")
        
        # Seção 2: Classificação
        st.subheader("2. Classificação")
        c3, c4, c5 = st.columns(3)
        tipo = c3.selectbox("Tipo de Documento *", ["Manuscrito", "Impresso", "Carta", "Fotografia", "Mapa", "Livro", "Outros"])
        idioma = c4.text_input("Idioma")
        periodo = c5.selectbox("Período Histórico *", ["Pré-história", "Antiguidade", "Medieval", "Moderno", "Contemporâneo"])
        
        # Seção 3: Datação
        st.subheader("3. Datação")
        c6, c7 = st.columns(2)
        data_precisa = c6.date_input("Data do Documento (Precisa)")
        data_approx = c7.text_input("Data Aproximada (Ex: 'c. 1800', 'Século XIX')")
        
        # Seção 4: Preservação
        st.subheader("4. Preservação")
        c8, c9, c10 = st.columns(3)
        repositorio = c8.text_input("Repositório")
        estado = c9.selectbox("Estado de Preservação", ["Excelente", "Bom", "Regular", "Ruim", "Crítico"])
        autenticidade = c10.selectbox("Status Autenticidade", ["Em análise", "Autêntico", "Incerto"])
        
        # Seção 5: Descrição
        st.subheader("5. Descrição e Conteúdo")
        descricao = st.text_area("Descrição Geral *", height=100)
        resumo = st.text_area("Resumo do Conteúdo")
        tags = st.text_input("Tags (separadas por vírgula)")
        
        # Seção 6: Arquivos
        st.subheader("6. Arquivos")
        arquivos = st.file_uploader("Upload de Imagens/PDFs", accept_multiple_files=True)
        
        submitted = st.form_submit_button("Salvar Documento")
        if submitted:
            st.success("Documento salvo com sucesso (Simulação)!")

# --- PÁGINA: ANÁLISE IA ---
elif menu_option == "Análise Inteligente (IA)":
    st.markdown("### Home > Análise Inteligente")
    st.title("Orisun AI Analyst")
    
    # Estado 1: Upload
    uploaded_file = st.file_uploader("Arraste sua fonte aqui (JPG, PDF)", type=['png', 'jpg', 'pdf'])
    
    if uploaded_file is not None:
        # Estado 2: Processamento Simulado
        with st.spinner('A Orisun está analisando a fonte e extraindo metadados...'):
            time.sleep(2) # Simulação
        
        # Estado 3: Validação Humana
        st.success("Análise concluída!")
        st.divider()
        
        # Toggle para esconder imagem (Recurso de Foco)
        show_image = st.checkbox("Mostrar Imagem Original", value=True)
        
        col_img, col_form = st.columns([1, 2] if show_image else [0.1, 3])
        
        if show_image:
            with col_img:
                st.image(uploaded_file, caption="Preview da Fonte", use_container_width=True)
        
        with col_form:
            st.subheader("🤖 Sugestão da IA")
            st.info("Confiança Alta: Título, Data | Confiança Baixa: Autor")
            
            # Formulário pré-preenchido
            st.text_input("Título Sugerido", value="Carta de Alforria - Manoel")
            st.date_input("Data Sugerida", value=date(1888, 5, 13))
            st.text_area("Resumo Extraído", value="Documento formal concedendo liberdade a...")
            
            col_b1, col_b2 = st.columns(2)
            if col_b1.button("✅ Aprovar e Salvar"):
                st.success("Salvo no Catálogo!")
            if col_b2.button("❌ Descartar"):
                st.rerun()

# --- PÁGINA: CATÁLOGO ---
elif menu_option == "Catálogo":
    st.markdown("### Home > Catálogo")
    c_head1, c_head2 = st.columns([3, 1])
    c_head1.title("Catálogo de Fontes")
    c_head2.button("Registrar Nova Fonte")
    
    # Toggle Visualização
    view_mode = st.radio("Visualização:", ["Grade", "Lista"], horizontal=True)
    
    if view_mode == "Grade":
        st.write("Exibindo em Grade...")
        col_g1, col_g2, col_g3 = st.columns(3)
        with col_g1:
            st.info("Imagem Doc 1")
            st.write("**Carta de 1889**")
            st.caption("Verificado por IA ✨")
        with col_g2:
            st.info("Imagem Doc 2")
            st.write("**Registro Civil**")
        with col_g3:
            st.info("Imagem Doc 3")
            st.write("**Foto Antiga**")
            
    else:
        st.write("Exibindo em Lista...")
        st.table([
            {"ID": 1, "Título": "Carta 1889", "Data": "1889", "Status": "Autêntico"},
            {"ID": 2, "Título": "Registro Civil", "Data": "1910", "Status": "Em análise"},
        ])
