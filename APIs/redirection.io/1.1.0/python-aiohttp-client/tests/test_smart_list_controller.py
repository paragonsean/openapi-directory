# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.smart_list import SmartList


pytestmark = pytest.mark.asyncio

async def test_get_smart_list_collection(client):
    """Test case for get_smart_list_collection

    Retrieves the collection of SmartList resources.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/smart-lists',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_smart_list_item(client):
    """Test case for get_smart_list_item

    Retrieves a SmartList resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/smart-lists/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

