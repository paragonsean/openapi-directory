# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_tickers_list_v2200_response import GetTickersListV2200Response
from openapi_server.models.get_tickers_v2200_response import GetTickersV2200Response


pytestmark = pytest.mark.asyncio

async def test_get_tickers_list_v2(client):
    """Test case for get_tickers_list_v2

    Get Tickers list V2
    """
    params = [('timestamp', '1519053802')]
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/tickers-list'.format(blockchain='bitcoin'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tickers_v2(client):
    """Test case for get_tickers_v2

    Get Tickers V2
    """
    params = [('timestamp', '1519053802'),
                    ('currency', 'usd')]
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/tickers'.format(blockchain='bitcoin'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

