# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inventory_list import InventoryList


pytestmark = pytest.mark.asyncio

async def test_inventory_get(client):
    """Test case for inventory_get

    Gets list of Inventory
    """
    params = [('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('pageSize', 56),
                    ('pageNumber', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Inventory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inventory_get_by_id(client):
    """Test case for inventory_get_by_id

    Gets InventoryItem by InventoryItem ID
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Inventory/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

