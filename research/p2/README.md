# Исходники P2

Здесь находятся файлы, которые описывают и воспроизводят стресс-тест научного контента.

```text
research/p2/
  build_assets.py       # генерирует PNG, Plotly HTML и bibliography
  references.bib        # исходная библиография
  alternatives/
    sphinx/index.rst    # вариант страницы для Sphinx + MyST
    quarto/p2.qmd       # вариант страницы для Quarto
```

Результаты скрипта намеренно не хранятся в Git:

```text
docs/assets/p2/         # графики, которые публикуются сайтом
docs/_generated/        # bibliography и manifest для MkDocs
```

Они создаются командой:

```bash
./.venv/Scripts/python.exe research/p2/build_assets.py
```

После этого сайт собирается обычной командой:

```bash
./.venv/Scripts/python.exe -m mkdocs build --strict
```