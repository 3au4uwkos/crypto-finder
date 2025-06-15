from framework import get_html
from bs4 import BeautifulSoup
import pandas as pd


def parse_html_to_dataframe(html: str, source: bool) -> pd.DataFrame:
    """Парсит HTML таблицу с обработкой специальных значений"""
    soup = BeautifulSoup(html, 'html.parser')

    if source:
        table = soup.find('table', {'class': 'sc-8b138daa-1 gEBUGZ'})
        if not table:
            raise ValueError("Таблица не найдена в HTML")

        rows = table.find_all('tr')[1:]
        data = []

        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 5:  # Проверяем, что есть хотя бы 9 колонок
                # Извлекаем нужные колонки
                name = cells[0].get_text(strip=True)
                roi_text = cells[5].get_text(strip=True)  # 6-я колонка (индекс 5)
                fund = cells[6].get_text(strip=True)  # 7-я колонка
                raise_text = cells[8].get_text(strip=True)[2:]  # 9-я колонка (индекс 8)


                # Проверка на пропуск строки
                if any(val in ['N/A', ''] for val in [roi_text, fund, raise_text]):
                    continue


                # Обработка ROI (удаляем 'x' и преобразуем в int)
                try:
                    roi = float(roi_text.rstrip('x'))
                except ValueError:
                    continue  # Пропускаем строку, если не удалось преобразовать


                # Обработка raise (K/M → тысячи/миллионы)
                try:
                    if 'K' in raise_text:
                        raise_val = float(raise_text.replace('K', '')) * 1000
                    elif 'M' in raise_text:
                        raise_val = float(raise_text.replace('M', '')) * 1000000
                    else:
                        raise_val = float(raise_text)
                except ValueError:
                    print(ValueError)
                    continue  # Пропускаем строку при ошибке преобразования

                data.append([name, roi, fund, raise_val])

        # Создаем DataFrame
        df = pd.DataFrame(data, columns=['name', 'roi', 'fund', 'raise'])

        # Преобразуем типы
        df['roi'] = df['roi'].astype(float)
        df['raise'] = df['raise'].astype(int)

    else:
        table = soup.find('table', {'class': 'sc-8b138daa-1 gEBUGZ'})
        if not table:
            raise ValueError("Таблица не найдена в HTML")

        rows = table.find_all('tr')[1:]
        data = []

        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 5:
                # Обработка name (cells[0])
                name = cells[0].get_text(strip=True)

                # Обработка raise (cells[3])
                raise_text = cells[3].get_text(strip=True)
                if raise_text == 'N/A':
                    raise_value = None
                else:
                    raise_text = raise_text.replace('$', '').replace(' ', '')
                    if 'K' in raise_text:
                        raise_value = float(raise_text.replace('K', '')) * 1000
                    elif 'M' in raise_text:
                        raise_value = float(raise_text.replace('M', '')) * 1000000
                    else:
                        raise_value = float(raise_text) if raise_text else None

                # Обработка fund (cells[4])
                fund = cells[4].get_text(strip=True)
                fund = fund if fund else None  # Пустая строка → None

                # Обработка date (cells[5])
                date_obj = cells[5].get_text(strip=True)


                data.append([name, raise_value, fund, date_obj])

    columns = ['name', 'roi', 'fund', 'raise'] if source else ['name', 'raise', 'fund', 'date']

    return pd.DataFrame(data, columns=columns)


def get_upcoming() -> pd.DataFrame:
    """Делает запросы к указанным страницам и объединяет результаты"""

    base_url = 'https://cryptorank.io/upcoming-ico'
    pages = [1,2]
    all_data = []

    for page in pages:
        url = f"{base_url}?rows=100&page={page}"
        print(f"🔄 Загружаем страницу {page}...")

        html = get_html(url)
        if html:
            try:
                df = parse_html_to_dataframe(html, source=False)
                all_data.append(df)
                print(f"✅ Страница {page} успешно обработана ({len(df)} записей)")
            except Exception as e:
                print(f"❌ Ошибка при обработке страницы {page}: {str(e)}")
        else:
            print(f"❌ Не удалось загрузить страницу {page}")

    # Объединение всех DataFrame
    if all_data:
        merged_df = pd.concat(all_data, ignore_index=True)
        print(f"\nОбъединено {len(all_data)} страниц, всего записей: {len(merged_df)}")
        return merged_df
    else:
        print("⚠️ Нет данных для объединения")
        return pd.DataFrame()

def get_source() -> pd.DataFrame:
    """Делает запросы к указанным страницам и объединяет результаты"""

    base_url = 'https://cryptorank.io/ico'
    pages = list(range(1, 44))
    all_data = []

    for page in pages:
        url = f"{base_url}?rows=100&page={page}"
        print(f"🔄 Загружаем страницу {page}...")

        html = get_html(url)
        if html:
            try:
                df = parse_html_to_dataframe(html, source=True)
                all_data.append(df)
                print(f"✅ Страница {page} успешно обработана ({len(df)} записей)")
            except Exception as e:
                print(f"❌ Ошибка при обработке страницы {page}: {str(e)}")
        else:
            print(f"❌ Не удалось загрузить страницу {page}")

    # Объединение всех DataFrame
    if all_data:
        merged_df = pd.concat(all_data, ignore_index=True)
        print(f"\nОбъединено {len(all_data)} страниц, всего записей: {len(merged_df)}")
        return merged_df
    else:
        print("⚠️ Нет данных для объединения")
        return pd.DataFrame()
