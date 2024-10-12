# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comic import Comic


pytestmark = pytest.mark.asyncio

async def test_comic_id_info0_json_get(client):
    """Test case for comic_id_info0_json_get

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/{comic_id}/info.0.json'.format(comic_id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_info0_json_get(client):
    """Test case for info0_json_get

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/info.0.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

