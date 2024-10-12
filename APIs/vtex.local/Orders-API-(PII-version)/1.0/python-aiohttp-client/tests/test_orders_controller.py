# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancel_order2200_response import CancelOrder2200Response
from openapi_server.models.cancel_order2_request import CancelOrder2Request
from openapi_server.models.get_order2200_response import GetOrder2200Response
from openapi_server.models.list_orders import ListOrders
from openapi_server.models.list_orders2_request import ListOrders2Request


pytestmark = pytest.mark.asyncio

async def test_cancel_order2(client):
    """Test case for cancel_order2

    Cancel order
    """
    body = openapi_server.CancelOrder2Request()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/orders/pvt/document/{order_id}/cancel'.format(order_id='70caf3941s6df1'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order2(client):
    """Test case for get_order2

    Get order
    """
    params = [('reason', 'data-validation')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/orders/pvt/document/{order_id}'.format(order_id='70caf3941s6df1'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_orders2(client):
    """Test case for list_orders2

    List orders
    """
    body = openapi_server.ListOrders2Request()
    params = [('f_hasInputInvoice', False)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/orders/extendsearch/orders',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_handling2(client):
    """Test case for start_handling2

    Start handling order
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/orders/pvt/document/{order_id}/actions/start-handling'.format(order_id='70caf3941s6df1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

