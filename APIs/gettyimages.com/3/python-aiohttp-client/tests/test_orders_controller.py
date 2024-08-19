# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.order_detail import OrderDetail


pytestmark = pytest.mark.asyncio

async def test_v3_orders_id_get(client):
    """Test case for v3_orders_id_get

    Get order metadata
    """
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/orders/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

