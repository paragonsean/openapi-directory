# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_public_history_get(client):
    """Test case for public_history_get

    Wetter 2021 für Berlin, Reichstag
    """
    params = [('q', 'Berlin, Reichstag'),
                    ('from', '2021-01-01'),
                    ('to', '2022-01-01')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/public/history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

