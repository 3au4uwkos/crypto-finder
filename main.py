from framework import get_html


def main():
    url = "https://github.com"  # Ваш URL

    print(f"🔄 Пробуем получить данные с {url}...")
    response = get_html(url)

    if response:
        print("\n✅ Данные получены!")
        print("Статус:", response.status_code)
        print("Размер HTML:", len(response.text), "символов")

        with open("output.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Сохранено в 'output.html'")
    else:
        print("\n❌ Все попытки исчерпаны. Сайт недоступен.")


if __name__ == "__main__":
    main()