# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_clicks_model import GetClicksModel


pytestmark = pytest.mark.asyncio

async def test_get_clicks(client):
    """Test case for get_clicks

    Get clicks
    """
    params = [('continueFrom', '1588788835614657618'),
                    ('limit', 1000)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/clicks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

