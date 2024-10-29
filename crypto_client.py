import aiohttp
import asyncio
from datetime import datetime


class DeribitClient:
    def __init__(self, base_url="https://www.deribit.com/api/v2"):
        self.base_url = base_url

    async def fetch_price(self, ticker):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/public/get_index_price?index_name={ticker}"
            async with session.get(url) as response:
                data = await response.json()
                return {
                    "ticker": ticker,
                    "price": data["result"]["index_price"],
                    "timestamp": datetime.utcnow().timestamp()
                }


async def main():
    client = DeribitClient()
    btc_price = await client.fetch_price("btc_usd")
    eth_price = await client.fetch_price("eth_usd")
    print(btc_price, eth_price)


asyncio.run(main())
