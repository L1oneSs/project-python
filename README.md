# Исследовательские материалы

Статический сайт на MkDocs для публикации учебных исследований. Основной отчёт доступен в [docs/assignment-1.md](docs/assignment-1.md), а команды запуска и публикации — в [docs/operations.md](docs/operations.md).

## Быстрый старт

```powershell
python -m virtualenv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Перед первым push замените демонстрационные адреса `site_url` и `repo_url` в `mkdocs.yml`. GitHub Pages использует workflow `pages.yml`; `helios-static-html.yml` собирает артефакт `helios-static-site` для подключения в Helios.