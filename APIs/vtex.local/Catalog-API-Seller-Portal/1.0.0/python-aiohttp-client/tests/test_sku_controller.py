# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_sku200_response import ListSKU200Response
from openapi_server.models.search_sku200_response import SearchSKU200Response


pytestmark = pytest.mark.asyncio

async def test_list_sku(client):
    """Test case for list_sku

    Get List of SKUs
    """
    params = [('from', '1'),
                    ('to', '50')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog-seller-portal/skus/ids',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_sku(client):
    """Test case for search_sku

    Search for SKU
    """
    params = [('from', '1'),
                    ('to', '50'),
                    ('id', 1),
                    ('externalid', 123456789)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog-seller-portal/skus/_search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

