# Подходы к публикации на GitHub Pages

Задание: разобраться в различии двух подходов к публикации статического сайта.

## 1. Push в ветку `gh-pages`

В этом варианте workflow собирает сайт в каталог `site/`, а action `peaceiris/actions-gh-pages` отправляет содержимое каталога в отдельную ветку `gh-pages`.

Пример шага:

```yaml
- name: Deploy to gh-pages
  uses: peaceiris/actions-gh-pages@v4
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    publish_dir: ./site
```

После этого в настройках Pages выбирается публикация из ветки `gh-pages`.

## 2. Официальная связка Pages Actions

Современный вариант использует два официальных action: `actions/upload-pages-artifact` загружает собранный сайт как артефакт, а `actions/deploy-pages` публикует этот артефакт через Pages deployment API.

Пример:

```yaml
- name: Upload artifact
  uses: actions/upload-pages-artifact@v3
  with:
    path: site

- name: Deploy to GitHub Pages
  uses: actions/deploy-pages@v4
```

Для этого способа в настройках репозитория выбирается **Settings → Pages → Source → GitHub Actions**.

## Сравнение

| Критерий | `peaceiris/actions-gh-pages` | `upload-pages-artifact` + `deploy-pages` |
| --- | --- | --- |
| Куда попадает результат сборки | В ветку `gh-pages` | Во временный Pages artifact |
| Требуется служебная ветка | Да | Нет |
| Способ настройки Pages | Ветка `gh-pages` | Источник `GitHub Actions` |
| Официальный механизм GitHub Pages | Нет, сторонний action | Да |

## Вывод

Оба подхода автоматизируют публикацию после push в `main`. `peaceiris/actions-gh-pages` делает публикацию через обычный push в ветку `gh-pages`, а официальная связка передаёт результат сборки в Pages без создания дополнительной ветки. В этом проекте используется официальный вариант, потому что он поддерживается GitHub и отделяет исходный код от опубликованного артефакта.