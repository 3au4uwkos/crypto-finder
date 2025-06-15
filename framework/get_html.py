import requests
import time
from typing import Optional


def get_html(url: str, max_retries: int = 100, delay: float = 3.5) -> Optional[requests.Response]:
    """
    Выполняет GET-запрос к указанному URL, повторяя попытки в случае неудачи.

    Параметры:
    - url (str): URL для запроса.
    - max_retries (int): Максимальное количество попыток (по умолчанию 100).
    - delay (float): Задержка между попытками в секундах (по умолчанию 3.5).

    Возвращает:
    - requests. Response: Объект ответа, если получен код 200.
    - None: Если все попытки исчерпаны.
    """
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response
            else:
                print(f"Попытка {retries + 1}: Получен код {response.status_code}. Повторная попытка...")
        except requests.exceptions.RequestException as e:
            print(f"Попытка {retries + 1}: Ошибка при запросе: {e}. Повторная попытка...")

        retries += 1
        if retries < max_retries:
            time.sleep(delay)

    print(f"Не удалось получить код 200 после {max_retries} попыток.")
    return None
