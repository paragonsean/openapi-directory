# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_api_card_get(client):
    """Test case for api_card_get

    Get Card
    """
    params = [('type', 'type_example')]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Card',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_card_types_get(client):
    """Test case for api_card_types_get

    Get available card types
    """
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Card/Types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

