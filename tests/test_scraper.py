import unittest
from src.scraper import get_result_urls

class TestScraper(unittest.TestCase):
    def test_get_result_urls(self):
        # Chama a função para obter as URLs
        urls = get_result_urls()

        # Verifica se o retorno é uma lista
        self.assertIsInstance(urls, list)

        # Verifica se a lista não está vazia
        self.assertTrue(len(urls) > 0)

        # Verifica se as URLs começam com "http"
        for url in urls:
            self.assertTrue(url.startswith("http"))

if __name__ == "__main__":
    unittest.main()