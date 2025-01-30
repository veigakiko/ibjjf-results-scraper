# IBJJF Results Scraper

Este projeto é um scraper desenvolvido em **Python** para coletar os resultados dos campeonatos da **IBJJF** (International Brazilian Jiu-Jitsu Federation). Utiliza **web scraping** para extrair os dados diretamente do site da IBJJF e armazená-los em um arquivo estruturado.

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
│-- README.md              # Documentação do projeto
│-- requirements.txt       # Dependências do projeto
│-- .gitignore             # Arquivos a serem ignorados pelo Git
```

---

## 🚀 Como Usar

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/ibjjf-results-scraper.git
cd ibjjf-results-scraper
```

### 2️⃣ Criar um Ambiente Virtual (Opcional)
```bash
python -m venv venv
```
**Ativar o ambiente:**
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 3️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o Scraper
```bash
python src/scraper.py
```

---

## 📊 Exemplo de Saída
O scraper gera um arquivo `.csv` com a seguinte estrutura:

| Year | Championship | Category | Position | Name | Academy |
|------|-------------|----------|----------|------|---------|
| 2024 | IBJJF World | Adult Black | 1st | João Silva | Gracie Barra |
| 2024 | IBJJF Pan | Master Blue | 3rd | Carlos Lima | Alliance |

---

## 🛠️ Tecnologias Utilizadas
- **Python**
- **Requests** - Para realizar as requisições HTTP.
- **BeautifulSoup** - Para fazer a extração dos dados da página HTML.
- **Pandas** - Para estruturar e manipular os dados.
- **TQDM** - Para exibir barras de progresso durante o scraping.
- **ThreadPoolExecutor** - Para paralelizar a coleta de dados.

---

## 📌 Melhorias Futuras
- Implementar **armazenamento em banco de dados**.
- Criar **dashboard interativo** para visualizar os resultados.
- Melhorar a **extração das categorias e pesos**.

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


