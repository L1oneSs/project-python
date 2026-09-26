# Исследовательские материалы

Статический сайт на MkDocs для публикации учебных исследований.

## Опубликованный сайт

- [GitHub Pages](https://l1oness.github.io/project-python/)
- [Helios ИТМО](https://se.ifmo.ru/~s506308/project-python/)


## Быстрый старт

```powershell
python -m virtualenv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m mkdocs serve
```

GitHub Pages использует workflow `pages.yml`, а `p4-helios.yml` собирает и публикует сайт на Helios через SSH с healthcheck, preview и rollback.