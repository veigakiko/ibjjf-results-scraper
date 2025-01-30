import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import time

# Definir caminho para salvar os dados
SAVE_PATH = r"C:\Users\Ricardo\Desktop\ibjjf-results-scraper\data"

# Criar a pasta caso não exista
os.makedirs(SAVE_PATH, exist_ok=True)

# Função para gerar a lista de URLs automaticamente
def get_result_urls(base_url="https://ibjjf.com/events/results"):
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        eventos = soup.find_all("a", class_="event-year-result")
        urls = []

        for evento in eventos:
            link = evento['href']
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
        soup = BeautifulSoup(response.text, 'html.parser')

        championship_tag = soup.find('h2', {"class": "title"})
        if championship_tag:
            championship_text = championship_tag.get_text(strip=True)
            year = ''.join(filter(str.isdigit, championship_text[-4:]))
        else:
            championship_text = "Championship not found"
            year = "Year not found"

        results = []
        elements = soup.find_all(['div', 'h4'], class_=['athlete-item', 'subtitle', 'position-athlete'])
        current_category, athlete_name, academy_name = None, None, None

        for elem in elements:
            if 'subtitle' in elem['class']:
                current_category = elem.get_text().strip()
            elif 'athlete-item' in elem['class']:
                athlete_details = elem.get_text().strip()
                athlete_name = athlete_details[:80].strip()
                academy_name = athlete_details[80:].strip()
            elif 'position-athlete' in elem['class']:
                position = elem.get_text().strip()
                results.append((year, championship_text, current_category, position, athlete_name, academy_name))

        return results
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL {url}: {e}")
        return []

# Função principal para scrape de resultados
def scrape_ibjjf_results(base_url="https://ibjjf.com/events/results"):
    start_time = time.time()
    print("Coletando URLs de resultados...")
    urls = get_result_urls(base_url)
    
    if not urls:
        print("Nenhuma URL encontrada. Encerrando...")
        return pd.DataFrame()

    print(f"{len(urls)} URLs encontradas. Iniciando processamento...")
    all_results = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(process_url, url): url for url in urls}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Processando URLs", unit="URL"):
            result = future.result()
            all_results.extend(result)

    end_time = time.time()
    print(f"Processamento concluído em {end_time - start_time:.2f} segundos.")

    if all_results:
        df = pd.DataFrame(all_results, columns=['Year', 'Championship', 'Category', 'Position', 'Name', 'Academy'])
        df['Category'] = df['Category'].astype(str)
        
        # Salvar o DataFrame na pasta especificada
        save_file = os.path.join(SAVE_PATH, "ibjjf_results.csv")
        df.to_csv(save_file, index=False, encoding='utf-8')
        print(f"Arquivo salvo em: {save_file}")
        
        return df
    else:
        print("Nenhum dado processado.")
        return pd.DataFrame()

# Executar o scraper
if __name__ == "__main__":
    df_ibjjf_scrap = scrape_ibjjf_results()
    if not df_ibjjf_scrap.empty:
        print("Exibindo os primeiros resultados:")
        print(df_ibjjf_scrap.head())
    else:
        print("Nenhum dado encontrado.")
