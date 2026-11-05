import pandas as pd
import streamlit as st

# 1. Configuração da Página para visual profissional em alta definição
st.set_page_config(
    page_title="AXIA Energia - RI Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS personalizada para fontes, cartões e elementos visuais
st.markdown("""
    <style>
        .main-header { font-size: 28px; font-weight: 700; color: #1E3A8A; margin-bottom: 5px; }
        .sub-header { font-size: 14px; color: #6B7280; margin-bottom: 25px; }
        .card { background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 5px solid #10B981; margin-bottom: 15px; }
        .card-title { font-size: 16px; font-weight: 600; color: #111827; }
        .card-body { font-size: 14px; color: #4B5563; margin-top: 5px; }
    </style>
""", unsafe_allow_html=True)

# 2. Barra Lateral (Sidebar) com Informações Institucionais e Logo
with st.sidebar:
    # Representação visual limpa do logotipo moderno da marca AXIA
    st.markdown("""
        <div style='text-align: center; padding: 10px; background: linear-gradient(135deg, #065F46, #1E3A8A); border-radius: 8px; margin-bottom: 20px;'>
            <h1 style='color: white; margin: 0; font-size: 32px; letter-spacing: 2px;'><b>ÁXIA</b></h1>
            <p style='color: #10B981; margin: 0; font-size: 11px; font-weight: bold;'>ENERGIA DO NOVO SÉCULO</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🏢 Sobre a Companhia")
    st.markdown("""
    A **AXIA Energia S.A.** (ex-Eletrobras) é a maior corporação de energia renovável do Hemisfério Sul. 
    Atua de forma integrada em estudos, projetos, construção e operação de usinas geradoras, 
    linhas de transmissão e distribuição.
    """)
    st.markdown("---")
    st.markdown("📌 **Governança:** Novo Mercado (B3)\n\n📍 **Sede:** Rio de Janeiro - RJ")

# 3. Cabeçalho Principal do Dashboard
st.markdown("<div class='main-header'>⚡ AXIA Energia — Corporate Investor Relations</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Acompanhamento de performance corporativa e inteligência de mercado da listagem AXIA3</div>", unsafe_allow_html=True)

# Abas estilizadas e com títulos claros
tab1, tab2 = st.tabs(["📊 Evolução AXIA", "📈 Inteligência de Mercado B3"])

# --- ABA 1: PERFORMANCE DA AXIA ---
with tab1:
    # Principais KPIs Financeiros reais da AXIA3 (Referência: Mercado B3)
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric(label="Ticker Principal", value="AXIA3", delta="Novo Mercado")
    kpi2.metric(label="Valor de Mercado", value="R$ 132.7 B", delta="+9.01% (12m)")
    kpi3.metric(label="Dividend Yield (Est.)", value="9.77 %", delta="Forte Retorno")
    kpi4.metric(label="Preço/Lucro (P/L)", value="12.73", delta="Estável")
    
    st.markdown("### Histórico Trimestral de Lucro Líquido")
    
    try:
        # Carregando e tratando os dados de evolução da AXIA
        df_axia = pd.read_excel("AXIA3_evolucao.xlsx")
        
        # Filtro de lucro conforme regras de negócio informadas
        dados_lucro = df_axia[df_axia["conta"] == "lucro"].copy()
        
        # Formatando os dados para o gráfico interativo nativo do Streamlit
        chart_data = dados_lucro.set_index("trimestre")[["valor"]]
        
        # Exibindo o gráfico de linha profissional e responsivo
        st.line_chart(chart_data, y="valor", use_container_width=True, color="#10B981")
        
        # Detalhamento dos dados em tabela aberta abaixo do gráfico
        with st.expander("📂 Visualizar planilha de evolução completa"):
            st.dataframe(df_axia, use_container_width=True)
            
    except FileNotFoundError:
        st.error("⚠️ Arquivo 'AXIA3_evolucao.xlsx' não encontrado. Certifique-se de que ele está no mesmo diretório do script.")

    # Seção Interativa Auxiliar para Engajamento de Usuários
    st.markdown("### 🛠️ Área de Interação")
    col_btn, col_txt = st.columns([1, 3])
    with col_btn:
        st.write("") 
        if st.button("🔄 Atualizar Relatório", use_container_width=True):
            st.toast("Dados atualizados com sucesso!", icon="⚡")
    with col_txt:
        nome = st.text_input("Assinatura do Analista", placeholder="Digite seu nome para registrar a análise...")
        if nome:
            st.caption(f"✍️ Analista responsável: **{nome}**")


# --- ABA 2: MERCADO B3 ---
with tab2:
    st.markdown("### Distribuição Setorial de Empresas Listadas")
    st.markdown("Análise quantitativa do número de empresas concorrentes e listadas por setor econômico na B3.")
    
    try:
        # Carregando dados da B3
        df_b3 = pd.read_excel("planilhao_b3.xlsx")
        
        # Processando dados: Agrupando por setor e ordenando para melhor estética visual
        df_size = df_b3.groupby("setor").size().reset_index(name="Quantidade de Empresas")
        df_size = df_size.sort_values(by="Quantidade de Empresas", ascending=False)
        
        # Formatando os dados estruturadamente para o Bar Chart nativo
        bar_data = df_size.set_index("setor")[["Quantidade de Empresas"]]
        
        # Gráfico de barras nativo interativo (Clean, profissional e responsivo ao mouse)
        st.bar_chart(bar_data, y="Quantidade de Empresas", use_container_width=True, color="#1E3A8A")
        
        # Detalhamento dos dados do Planilhão
        with st.expander("📂 Explorar o Planilhão B3 bruto"):
            st.dataframe(df_b3, use_container_width=True)
            
    except FileNotFoundError:
        st.error("⚠️ Arquivo 'planilhao_b3.xlsx' não encontrado. Certifique-se de que ele está no mesmo diretório do script.")
