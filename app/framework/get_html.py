import time
from typing import Optional
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def get_html(url: str, max_retries: int = 3, delay: float = 3.5) -> Optional[str]:
    """
    Получает HTML-содержимое страницы с использованием Playwright.

    Параметры:
    - url (str): URL для запроса.
    - max_retries (int): Максимальное количество попыток (по умолчанию 5).
    - delay (float): Задержка между попытками в секундах (по умолчанию 3.5).

    Возвращает:
    - str: HTML-содержимое страницы при успехе.
    - None: Если все попытки исчерпаны.
    """
    retries = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        while retries < max_retries:
            try:
                page = browser.new_page(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                )

                page.goto(url, timeout=30000)
                page.wait_for_selector('tbody', timeout=10000)
                html = page.content()
                browser.close()
                return html

            except PlaywrightTimeoutError:
                print(f"Попытка {retries + 1}: Таймаут при загрузке страницы. Повторная попытка...")
            except Exception as e:
                print(f"Попытка {retries + 1}: Ошибка: {str(e)}. Повторная попытка...")

            retries += 1
            if retries < max_retries:
                time.sleep(delay)

    print(f"Не удалось получить данные после {max_retries} попыток.")
    return None
