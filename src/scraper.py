import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import time  # Para medir o tempo de execução

# Função para gerar a lista de URLs automaticamente
def get_result_urls(base_url="https://ibjjf.com/events/results"):
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        # Encontrar todos os links de resultados
        eventos = soup.find_all("a", class_="event-year-result")
        urls = []

        for evento in eventos:
            link = evento['href']
            # Verificar se o link é absoluto ou relativo
            if not link.startswith("http"):
                link = "https://ibjjf.com" + link
            urls.append(link)

        return urls
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página base: {e}")
        return []

# Função para processar uma única URL de resultados
def process_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # Extração do título do campeonato e ano
        championship_tag = soup.find('h2', {"class": "title", "style": "border-bottom: none !important; padding-top: 1%; padding-bottom: 1.5%;"})
        if championship_tag:
            championship_text = championship_tag.get_text(strip=True)
            year = ''.join(filter(str.isdigit, championship_text[-4:]))  # Assume que o ano está nos últimos 4 caracteres
        else:
            championship_text = "Championship not found"
            year = "Year not found"

        results = []  # Lista para armazenar resultados de cada página

        # Iterar sobre elementos
        elements = soup.find_all(['div', 'h4'], class_=['athlete-item', 'subtitle', 'position-athlete'])
        current_category = None
        athlete_name = None
        academie_name = None

        for elem in elements:
            if 'subtitle' in elem['class']:
                current_category = elem.get_text().strip()
            elif 'athlete-item' in elem['class']:
                athlete_details = elem.get_text().strip()
                athlete_name = athlete_details[52:132].strip()  # Ajustar conforme necessário
                academie_name = athlete_details[200:].strip()
            elif 'position-athlete' in elem['class']:
                position = elem.get_text().strip()
                results.append((year, championship_text, current_category, position, athlete_name, academie_name))

        return results
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL {url}: {e}")
        return []

# Função principal para scrape de resultados
def scrape_ibjjf_results(base_url="https://ibjjf.com/events/results"):
    start_time = time.time()  # Marcar o início do processamento

    print("Coletando URLs de resultados...")
    urls = get_result_urls(base_url)  # Obter URLs automaticamente
    if not urls:
        print("Nenhuma URL encontrada. Encerrando...")
        return pd.DataFrame()

    print(f"{len(urls)} URLs encontradas. Iniciando processamento...")
    all_results = []  # Lista para todos os resultados

    # Usar paralelismo para processar URLs
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(process_url, url): url for url in urls}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Processando URLs", unit="URL"):
            result = future.result()
            all_results.extend(result)

    end_time = time.time()  # Marcar o fim do processamento

    print(f"Processamento concluído em {end_time - start_time:.2f} segundos.")

    # Criar DataFrame a partir dos resultados
    if all_results:
        df = pd.DataFrame(all_results, columns=['Year', 'Championship', 'Category', 'Position', 'Name', 'Academy'])
        split_data = df['Category'].str.split(r'\s*/\s*|\s*\(\s*|\s*lb\s*\)', expand=True)
        df[['Gender', 'Age Group', 'Belt Color', 'Weight Class', 'Weight']] = split_data.iloc[:, :5]
        df['Weight'] = df['Weight'].str.strip()
        df.drop(columns=['Category'], inplace=True)
        return df
    else:
        print("Nenhum dado processado.")
        return pd.DataFrame()

# Exemplo de uso
if __name__ == "__main__":
    start_time = time.time()  # Tempo total do script
    df_ibjjf_scrap = scrape_ibjjf_results()

    if not df_ibjjf_scrap.empty:
        print("Exibindo os primeiros resultados:")
        print(df_ibjjf_scrap.head())
    else:
        print("Nenhum dado encontrado.")

    end_time = time.time()  # Tempo total do script
    print(f"Tempo total do script: {end_time - start_time:.2f} segundos.")
