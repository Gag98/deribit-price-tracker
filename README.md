Crypto API Project

Асинхронный клиент на aiohttp для получения данных о ценах валют `btc_usd` и `eth_usd` с криптобиржи Deribit и
сохранения их в базу данных.
FastAPI API предоставляет доступ к сохранённым данным с фильтрацией.

1. Клонируйте репозиторий.
2. Установите зависимости: `pip install -r requirements.txt`.

- Для локального запуска:
  ```bash
  uvicorn api:app --reload

