# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.numbers_v2_bulk_hosted_number_order import NumbersV2BulkHostedNumberOrder


pytestmark = pytest.mark.asyncio

async def test_fetch_bulk_hosted_number_order(client):
    """Test case for fetch_bulk_hosted_number_order

    
    """
    params = [('OrderStatus', 'order_status_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/HostedNumber/Orders/Bulk/{bulk_hosting_sid}'.format(bulk_hosting_sid='bulk_hosting_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

