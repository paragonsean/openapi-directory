# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.token_price import TokenPrice


pytestmark = pytest.mark.asyncio

async def test_get_token_price(client):
    """Test case for get_token_price

    Lists price and available volume for a certain token
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/tokens/prices/{token_id}'.format(token_id='token_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_token_prices(client):
    """Test case for get_token_prices

    Lists all token prices and available volume
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/tokens/prices/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

