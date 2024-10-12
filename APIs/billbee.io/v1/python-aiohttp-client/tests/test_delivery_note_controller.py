# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_order_api_create_delivery_note_0(client):
    """Test case for order_api_create_delivery_note_0

    Create an delivery note for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.
    """
    params = [('includePdf', True),
                    ('sendToCloudId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orders/CreateDeliveryNote/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

