# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.store_single import StoreSingle
from openapi_server.models.stores_list200_response import StoresList200Response


pytestmark = pytest.mark.asyncio

async def test_stores_list(client):
    """Test case for stores_list

    Get a list of video game storefronts.
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/stores',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stores_read(client):
    """Test case for stores_read

    Get details of the store.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/stores/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

