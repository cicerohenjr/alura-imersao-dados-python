# 🐍 Imersão Dados com Python (Alura)

Este repositório documenta minha jornada de aprendizado na Imersão Dados, começando pelos fundamentos da linguagem Python até a análise de dados complexos.

## 📂 Módulos do Projeto

### [Aula 00: Fundamentos e Lógica](./aula00_fundamentos/aula00_introducao.ipynb)
Nesta aula introdutória, foquei em entender a sintaxe base do Python antes de partir para a análise de dados.
- **Variáveis:** Tipagem forte e dinâmica (`str`, `int`, `float`).
- **Boas Práticas:** Adoção do padrão **Snake Case** (`nome_variavel`) para legibilidade, seguindo a PEP 8.
- **Lógica Condicional:** Entendimento profundo sobre como a **identação** define os blocos de execução no `if/else`.
  - *Exemplo prático:* Algoritmo de verificação de habilitação (CNH).

---
---
### [Aula 01: Análise de Dados com Pandas](./aula01_analise_dados/aula01_analise_salarios.ipynb)
Iniciamos a manipulação de dados reais utilizando a biblioteca **Pandas**.
- **Leitura de Dados:** Importação de arquivo CSV direto do repositório.
- **Tratamento:** Renomeação de colunas (tradução EN -> PT) para facilitar a leitura.
- **Estatística Descritiva:** Uso do `describe()` e `info()` para entender a distribuição salarial e os tipos de dados.

### [Aula 02: Limpeza e Tratamento de Dados](./aula02_tratamento_dados/aula02_tratamento_dados.ipynb)
Nesta etapa, focamos na preparação da base para análise, removendo inconsistências.
- **Detecção de Nulos:** Uso do `isnull().sum()` para identificar dados ausentes.
- **Estratégias de Tratamento:** Testes com Média, Mediana e métodos de continuidade (`ffill`, `bfill`).
- **Limpeza Final:** Remoção de dados inconsistentes com `dropna()`.
- **Conversão de Tipos:** Ajuste da coluna `ano` de `float` para `int64` para corrigir a formatação.

### [Aula 03: Gráficos e Visualização de Dados](./aula03_analise_visual/aula03_graficos_visuais.ipynb)
Transformação de dados em insights visuais utilizando três bibliotecas poderosas.
- **Pandas Plot:** Visualizações rápidas (`.plot()`).
- **Seaborn & Matplotlib:** Gráficos estáticos avançados (Barras, Histograma e Boxplot) com personalização de cores e tamanhos.
- **Plotly Express:** Gráficos interativos (Barras e Rosca) para dashboards.
- **Desafio:** Análise de salário médio de *Data Scientists* por país.

---*Desenvolvido por Cícero Henrique durante a Imersão Dados 2026.*


