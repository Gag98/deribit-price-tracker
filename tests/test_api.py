import pytest
from httpx import AsyncClient, ASGITransport
from api import app

@pytest.mark.asyncio
async def test_get_all_prices():
    transport = ASGITransport(app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/prices/?ticker=btc_usd")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_last_price():
    transport = ASGITransport(app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/prices/last/?ticker=btc_usd")
    assert response.status_code == 200
    assert isinstance(response.json(), dict) or response.json() is None

