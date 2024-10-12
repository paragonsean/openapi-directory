# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_city_get(client):
    """Test case for city_get

    
    """
    params = [('key', 'key_example'),
                    ('lng', 3.4),
                    ('lat', 3.4),
                    ('format', 'format_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/city',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

