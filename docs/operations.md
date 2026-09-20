# Эксплуатация

## Ежедневный цикл

1. Активировать `.venv`.
2. Запустить `python -m mkdocs serve` и проверить страницу локально.
3. Выполнить `python -m mkdocs build --strict`.
4. Добавить новый Markdown-файл и пункт навигации.
5. Создать коммит и отправить его в `main`.

## Настройка адресов

Замените демонстрационные значения в `mkdocs.yml`:

```yaml
site_url: https://USERNAME.github.io/REPOSITORY/
repo_url: https://github.com/USERNAME/REPOSITORY
```

Для Helios укажите адрес проекта вместе с подкаталогом, который выдаёт платформа. Не добавляйте завершающий путь вручную в ссылки Markdown: MkDocs сформирует их из `site_url`.