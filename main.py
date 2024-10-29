import asyncio
from database import init_db
from crypto_client import DeribitClient
from save_data import save_price


async def fetch_and_save():
    client = DeribitClient()
    while True:
        for ticker in ["btc_usd", "eth_usd"]:
            data = await client.fetch_price(ticker)
            await save_price(data)
        await asyncio.sleep(60)


async def main():
    await init_db()
    await fetch_and_save()


if __name__ == "__main__":
    asyncio.run(main())
