# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.order_list_full import OrderListFull
from openapi_server.models.order_list_light import OrderListLight
from openapi_server.models.order_list_request import OrderListRequest


pytestmark = pytest.mark.asyncio

async def test_get_order_list_full(client):
    """Test case for get_order_list_full

    [DEPRECATED] Get a paginated list of all Orders with all Order and Order Item(s) properties
    """
    body = openapi_server.OrderListRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_encoding': ['accept_encoding_example'],
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/list/full',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order_list_light(client):
    """Test case for get_order_list_light

    [DEPRECATED] Get a paginated list of all Orders without details
    """
    body = openapi_server.OrderListRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/list/light',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

