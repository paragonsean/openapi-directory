# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_inventory_notification(client):
    """Test case for inventory_notification

    Notify marketplace of inventory update
    """
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/notificator/{seller_id}/changenotification/{sku_id}/inventory'.format(seller_id='seller123', sku_id='1234'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_price_notification(client):
    """Test case for price_notification

    Notify marketplace of price update
    """
    params = [('accountName', 'apiexamples'),
                    ('environment', 'vtexcommercestable')]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/notificator/{seller_id}/changenotification/{sku_id}/price'.format(seller_id='seller123', sku_id='1234'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

