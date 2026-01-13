# 🚀 Projeto 3: Dashboard Interativo (Grand Finale)

Este é o **Grand Finale** da trilha de projetos: um Dashboard Interativo de Vendas desenvolvido com **Python** e **Streamlit**. 

O objetivo é transformar dados brutos (`csv`) em insights visuais, permitindo a análise de performance por estado, categoria e métricas financeiras (KPIs) em tempo real.

## 📊 Funcionalidades

* **KPIs em Destaque:** Visualização imediata de Faturamento Total, Quantidade de Produtos e Ticket Médio.
* **Filtros Dinâmicos:** Barra lateral para filtrar dados por **Estado** e **Categoria**.
* **Gráficos Interativos:** * Gráfico de Barras (Faturamento por Estado).
    * Gráfico de Pizza (Distribuição de Vendas por Categoria).
* **Tabela de Dados:** Visualização analítica da base de dados filtrada.

## 🛠️ Tecnologias 

* **Python 3**
* **Streamlit:** Para a interface web interativa.
* **Pandas:** Para manipulação e análise de dados.
* **Plotly Express:** Para geração dos gráficos.


## 🚀 Como Rodar O Projeto 

* **Clone este repositório**
git clone [https://github.com/SEU-USUARIO/projeto-3.git](https://github.com/SEU-USUARIO/projeto-3.git)

# (Opcional) Crie e ative um ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instale as bibliotecas necessárias
pip install streamlit pandas plotly

# Rode exececutando esse comando
streamlit run app.py

## 📂 Estrutura do Projeto

```bash
projeto-3/
├── app.py              # Código principal do Dashboard
├── dados_vendas.csv    # Base de dados (Fonte)
├── README.md           # Documentação

--- 

**Desenvolvido por Alebazi**