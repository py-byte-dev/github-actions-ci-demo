import pytest
from httpx import ASGITransport, AsyncClient
from api.main import app


@pytest.mark.asyncio
async def test_random_number():
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/random-text")

    assert response.status_code == 200
    data = response.json()
    assert "number" in data
    assert isinstance(data["number"], int)
    assert 1 <= data["number"] <= 100
