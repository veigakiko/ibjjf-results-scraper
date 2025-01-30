# IBJJF Results Scraper

Este projeto é um scraper desenvolvido em **Python** para coletar os resultados dos campeonatos da **IBJJF** (International Brazilian Jiu-Jitsu Federation). Utiliza **web scraping** para extrair os dados diretamente do site da IBJJF e armazená-los em um arquivo estruturado.

## 📖 Visão Geral
Este projeto realiza scraping dos resultados dos campeonatos de Jiu-Jitsu organizados pela IBJJF. Os dados extraídos podem ser utilizados para análises estatísticas, rankings e históricos de desempenho.

🔹 **Fonte:** [IBJJF Results](https://ibjjf.com/events/results)  
🔹 **Formato dos Dados:** CSV estruturado  
🔹 **Finalidade:** Estudos sobre desempenho de atletas, análise de academias e estatísticas do esporte  

## 📌 Funcionalidades
- Extração automática dos resultados de campeonatos da IBJJF.
- Paralelização para acelerar a coleta dos dados.
- Processamento e estruturação das informações em um **DataFrame Pandas**.
- Exportação dos resultados para análise posterior.

---

## 📦 Estrutura do Projeto

```
ibjjf-results-scraper/
│-- data/                  # Armazena os resultados extraídos
│-- src/                   # Código-fonte do projeto
│   │-- scraper.py         # Código principal de web scraping
│-- notebooks/             # Notebooks para análise e testes
│-- logs/                  # Armazena logs da execução
│-- assets/                # Imagens ou recursos para documentação
│-- README.md              # Documentação do projeto
│-- requirements.txt       # Dependências do projeto
│-- .gitignore             # Arquivos a serem ignorados pelo Git
```

### 🛠 Criando a Estrutura do Projeto
Para criar manualmente a estrutura do projeto e gerar automaticamente o arquivo `requirements.txt`, execute os seguintes comandos:

```bash
mkdir ibjjf-results-scraper
cd ibjjf-results-scraper
mkdir data src notebooks logs assets
cd src
touch scraper.py
cd ..
touch README.md .gitignore

echo "requests" >> requirements.txt
echo "beautifulsoup4" >> requirements.txt
echo "pandas" >> requirements.txt
echo "tqdm" >> requirements.txt
```

---

## 🚀 Como Usar

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/veigakiko/ibjjf-results-scraper.git
cd ibjjf-results-scraper
```

### 2️⃣ Criar e Ativar um Ambiente Virtual
```bash
python -m venv venv
```
**Ativar o ambiente:**
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

**Verificar se o ambiente está ativo:**
```bash
python --version
```

### 3️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o Scraper
```bash
python src/scraper.py
```

### 5️⃣ Acessar os Dados Extraídos
Os resultados coletados serão salvos automaticamente em:

```plaintext
C:\Users\Ricardo\Desktop\ibjjf-results-scraper\data\ibjjf_results.csv
```

---

## 📊 Exemplo de Saída
O scraper gera um arquivo `.csv` com a seguinte estrutura:

| Year | Championship | Category | Position | Name | Academy |
|------|-------------|----------|----------|------|---------|
| 2024 | IBJJF World | Adult Black | 1st | João Silva | Gracie Barra |
| 2024 | IBJJF Pan | Master Blue | 3rd | Carlos Lima | Alliance |

---

## 📝 Logs da Execução
Durante a execução do scraper, logs são gerados automaticamente para facilitar o monitoramento de erros e progresso.

- Os logs são salvos na pasta `logs/`.
- Para visualizar os logs enquanto o scraper roda:
```bash
tail -f logs/scraper.log
```

---

## 🛠️ Tecnologias Utilizadas
- **Python**
- **Requests** - Para realizar as requisições HTTP.
- **BeautifulSoup** - Para fazer a extração dos dados da página HTML.
- **Pandas** - Para estruturar e manipular os dados.
- **TQDM** - Para exibir barras de progresso durante o scraping.
- **ThreadPoolExecutor** - Para paralelizar a coleta de dados.

---

## 📌 Melhorias Futuras (To-Do List)
- [ ] Implementar **armazenamento em banco de dados** (PostgreSQL ou MongoDB)
- [ ] Criar **dashboard interativo** para visualizar os resultados dos atletas.
- [ ] Melhorar a **extração das categorias e pesos** para evitar inconsistências.
- [ ] Implementar um **modo de agendamento automático** para atualizar os dados periodicamente.
- [ ] Adicionar suporte para exportação dos dados em **JSON e Excel**.

---

## 📜 Licença
Este projeto está licenciado sob a **MIT License**. Sinta-se à vontade para contribuir!

---

## 💡 Contribuição
Contribuições são bem-vindas! Para contribuir:
1. Faça um **fork** do repositório.
2. Crie uma **branch** (`feature-nova-funcionalidade`).
3. Faça um **commit** das suas alterações.
4. Envie um **pull request**.

Vamos juntos melhorar esse projeto! 🚀

