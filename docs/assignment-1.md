# Задание 1. Генераторы статических сайтов

## Цель и выбранный инструмент

Для публикации исследовательских материалов выбран **MkDocs** — генератор статических сайтов на Python. Он принимает Markdown-файлы, строит HTML без серверной части и хорошо подходит для GitHub Pages и статического хостинга.

Преимущества для учебного проекта:

- отчёт хранится рядом с исходным кодом и изменяется обычным Git-коммитом;
- навигация описывается в одном YAML-файле;
- встроенный поиск Material for MkDocs работает на стороне браузера;
- строгая сборка позволяет остановить публикацию при предупреждении или битой ссылке.

## Выполнение пунктов

### 1–3. Python и виртуальное окружение

Проверенная конфигурация:

```text
Python 3.13.5
pip 25.1.1
virtualenv 20.x
```

Создание окружения в Windows PowerShell:

```powershell
python -m virtualenv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Для CMD используется `.venv\Scripts\activate.bat`.

### 4–5. Зависимости и каркас

Версии зафиксированы в `requirements.txt`. Каталоги виртуального окружения, кэш и результат сборки исключены в `.gitignore`. Каркас сайта состоит из `docs/`, `mkdocs.yml` и отдельных Markdown-страниц.

### 6. Локальная сборка

Для предпросмотра:

```powershell
python -m mkdocs serve
```

Для проверки перед публикацией:

```powershell
python -m mkdocs build --strict
```

Ключ `--strict` превращает предупреждения MkDocs в ошибку и поэтому используется в CI.

### 7. Git и GitHub

После создания пустого репозитория на GitHub:

```powershell
git init
git add .
git commit -m "Initialize MkDocs research site"
git branch -M main
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git push -u origin main
```

В `mkdocs.yml` нужно заменить `site_url` и `repo_url` на адреса своего репозитория.

### 8. GitHub Actions и два способа публикации

В репозитории нужно открыть **Settings → Pages → Build and deployment → Source → GitHub Actions**. Файл `pages.yml` использует официальный современный вариант: `actions/upload-pages-artifact` передаёт собранный каталог в `actions/deploy-pages`.

Альтернативный вариант — `peaceiris/actions-gh-pages`: он коммитит содержимое `site/` в ветку `gh-pages`, после чего Pages публикует эту ветку. Этот подход проще концептуально, но создаёт служебную ветку и отдельный push. В данном проекте выбран официальный artifact-based workflow.

### 9–10. Helios ИТМО и Static HTML

Аккаунт Helios ИТМО публикует файлы из `~/public_html`. Workflow `helios-static-html.yml` собирает сайт в строгом режиме, сохраняет артефакт `helios-static-site`, передаёт архив по SSH и распаковывает его в `~/public_html/project-python`. Публичный адрес проекта: `https://se.ifmo.ru/~s506308/project-python/`.

Перед первым запуском добавьте в GitHub секрет `HELIOS_PASSWORD` через **Settings → Secrets and variables → Actions → New repository secret**. Сам пароль не должен находиться в YAML, Git-коммитах или тексте отчёта. Workflow использует порт SSH `2222` и очищает только содержимое каталога проекта `~/public_html/project-python`.

### 11. URL и подкаталог

В `mkdocs.yml` заданы:

```yaml
site_url: !ENV [SITE_URL, 'https://l1oness.github.io/project-python/']
use_directory_urls: false
```

Для GitHub Pages используется значение по умолчанию, а Helios workflow передаёт `SITE_URL=https://se.ifmo.ru/~s506308/project-python/`. `use_directory_urls: false` генерирует явные `.html`-адреса и уменьшает риск 404 при размещении в подкаталоге. Если путь на Helios изменится, достаточно изменить переменную `SITE_URL` в workflow.

### 12. Проверки опубликованного сайта

Минимальный чек-лист:

```powershell
curl.exe -I https://USERNAME.github.io/REPOSITORY/
curl.exe https://USERNAME.github.io/REPOSITORY/ | Select-String "Исследовательские материалы"
```

Также нужно проверить поиск, открыть страницу отчёта напрямую и убедиться, что формула ниже остаётся читаемой при отключённом CDN:

$$E = mc^2$$

MathJax подключён в конфигурации как внешний ресурс. Для полностью автономного режима его следует скачать в `docs/assets/` и заменить URL на локальный файл; это отдельное улучшение перед публикацией в среде с ограниченным доступом в Интернет.

### 13. Лицензирование

- Текст и результаты исследований: **CC BY 4.0**, файл `LICENSE-CONTENT-CC-BY-4.0`.
- Конфигурация, workflow и прочий код: **MIT**, файл `LICENSE-CODE-MIT`.

При добавлении чужих изображений, данных или фрагментов кода их источники и отдельные лицензии нужно указывать на странице соответствующего исследования.

### 14. Отладка

| Симптом | Причина | Исправление |
| --- | --- | --- |
| `No module named mkdocs` | Команда запускается вне `.venv` | Активировать окружение или использовать `.venv\Scripts\python.exe -m mkdocs` |
| Сборка CI падает на предупреждении | Включён строгий режим | Исправить ссылку или заголовок, затем повторить `mkdocs build --strict` |
| GitHub Pages открывает пустую страницу | Не выбран Pages source | Установить `Source = GitHub Actions` |
| На Helios 404 во внутренних ссылках | Сайт опубликован в подкаталоге | Проверить `site_url` и оставить `use_directory_urls: false` |
| Формулы пропали без сети | Используется внешний MathJax CDN | Подключить локальную копию MathJax и проверить offline-сборку |

## Вывод

MkDocs закрывает задачу публикации исследовательских результатов с небольшим количеством инфраструктуры. После добавления нового файла в `docs/research/` его нужно включить в `nav` в `mkdocs.yml`, проверить строгую сборку и отправить коммит в `main`; GitHub Actions соберёт и опубликует обновлённый сайт.