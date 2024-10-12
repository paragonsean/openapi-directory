# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_blockchain200_response import GetBlockchain200Response


pytestmark = pytest.mark.asyncio

async def test_get_available_blockchains(client):
    """Test case for get_available_blockchains

    List available blockchains
    """
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_blockchain(client):
    """Test case for get_blockchain

    Blockchain Info Summary
    """
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}'.format(blockchain='bitcoin'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

