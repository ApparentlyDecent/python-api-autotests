# Автоматизированное тестирование REST API

## О проекте

Учебный проект по автоматизации тестирования REST API с использованием Python, pytest и requests.

В проекте реализованы автотесты для проверки API интернет-магазина DummyJSON.

## Технологии

- Python
- pytest
- requests
- pytest-html

## API

Для тестирования используется [DummyJSON Products API](https://dummyjson.com/products).

## Что проверяют тесты

### Получение товаров (`test_products.py`)
- Получение списка товаров.
- Проверка структуры ответа.
- Получение товара по ID.
- Проверка несуществующих и некорректных ID.

### Поиск товаров (`test_product_search.py`)
- Поиск товаров по ключевым словам.
- Поиск с несколькими поисковыми запросами.
- Проверка поиска без результатов.
- Проверка пустого поискового запроса.

### Пагинация (`test_pagination.py`)
- Получение товаров с использованием `limit` и `skip`.
- Проверка перехода между страницами.
- Проверка запроса за пределами доступного диапазона.
- Проверка некорректных значений `limit`.

## Структура проекта

```text
python-api-autotests/
├── tests/
│   ├── conftest.py
│   ├── test_products.py
│   ├── test_product_search.py
│   └── test_pagination.py
├── .gitignore
├── config.py
├── requirements.txt
└── README.md
```

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/ApparentlyDecent/python-api-autotests.git
cd python-api-autotests
```

### 2. Создание виртуального окружения

```bash
python -m venv .venv
```

Активация в Windows:

```bash
.venv\Scripts\activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Запуск тестов

```bash
python -m pytest -v
```

## HTML-отчёт

Для генерации HTML-отчёта используется pytest-html:

```bash
python -m pytest --html=report.html
```

После выполнения команды отчёт будет сохранён в корневой папке проекта.