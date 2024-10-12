# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_block_hash_v2200_response import GetBlockHashV2200Response
from openapi_server.models.get_block_v2200_response import GetBlockV2200Response
from openapi_server.models.get_raw_block_v2200_response import GetRawBlockV2200Response


pytestmark = pytest.mark.asyncio

async def test_get_block_hash_v2(client):
    """Test case for get_block_hash_v2

    Get block hash V2
    """
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/block-index/{block_height}'.format(blockchain='bitcoin', block_height=15),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_block_v2(client):
    """Test case for get_block_v2

    Get Block V2
    """
    params = [('page', 1),
                    ('pageSize', 1000)]
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/block/{block_hash_or_height}'.format(blockchain='bitcoin', block_hash_or_height='00000000000000000035835503f43c878ebb643f3b40bdfd0dfda760da74e73c'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_raw_block_v2(client):
    """Test case for get_raw_block_v2

    Get raw block data V2
    """
    headers = { 
        'Accept': 'application/json',
        'X-RapidAPI-Host': 'special-key',
        'X-API-Key': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/{blockchain}/v2/rawblock/{block_hash_or_height}'.format(blockchain='bitcoin', block_hash_or_height='00000000000000000035835503f43c878ebb643f3b40bdfd0dfda760da74e73c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

