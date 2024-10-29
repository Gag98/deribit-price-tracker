from database import async_session, prices

async def save_price(data):
    async with async_session() as session:
        async with session.begin():
            query = prices.insert().values(
                ticker=data["ticker"],
                price=data["price"],
                timestamp=data["timestamp"]
            )
            await session.execute(query)
