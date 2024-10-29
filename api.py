from fastapi import FastAPI
from database import async_session, prices
from sqlalchemy.future import select

app = FastAPI()


@app.get("/prices/")
async def get_all_prices(ticker: str):
    async with async_session() as session:
        query = select(prices).where(prices.c.ticker == ticker)
        result = await session.execute(query)
        return [dict(row) for row in
                result.mappings()]


@app.get("/prices/last/")
async def get_last_price(ticker: str):
    async with async_session() as session:
        query = select(prices).where(prices.c.ticker == ticker).order_by(prices.c.timestamp.desc()).limit(1)
        result = await session.execute(query)
        row = result.mappings().first()
        return dict(row) if row is not None else None


@app.get("/prices/by_date/")
async def get_prices_by_date(ticker: str, start_date: int, end_date: int):
    async with async_session() as session:
        query = select(prices).where(
            (prices.c.ticker == ticker) &
            (prices.c.timestamp >= start_date) &
            (prices.c.timestamp <= end_date)
        )
        result = await session.execute(query)
        return [dict(row) for row in
                result.mappings()]
