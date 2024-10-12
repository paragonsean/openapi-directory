# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_suggestion(client):
    """Test case for get_suggestion

    Get SKU Suggestion by ID
    """
    params = [('accountName', 'apiexamples')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/suggestions/{seller_id}/{seller_sku_id}'.format(seller_id='seller123', seller_sku_id='1234'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getsuggestions(client):
    """Test case for getsuggestions

    Get all SKU suggestions
    """
    params = [('accountName', 'apiexamples'),
                    ('q', ''),
                    ('type', 'new'),
                    ('seller', ''),
                    ('status', 'accepted'),
                    ('hasmapping', 'true'),
                    ('matcherid', 'vtex-matcher'),
                    ('_from', 1),
                    ('_to', 50)]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/suggestions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

