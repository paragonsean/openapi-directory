# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.error_response_message import ErrorResponseMessage
from openapi_server.models.order_list_full_with_links import OrderListFullWithLinks
from openapi_server.models.order_list_light_with_links import OrderListLightWithLinks
from openapi_server.models.order_list_request import OrderListRequest


pytestmark = pytest.mark.asyncio

async def test_get_order_list_full_v3(client):
    """Test case for get_order_list_full_v3

    Get a paginated list of all Orders with all Order and Order Item(s) properties
    """
    body = openapi_server.OrderListRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_encoding': 'accept_encoding_example',
    }
    response = await client.request(
        method='POST',
        path='/orders/v3/list/full',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order_list_light_v3(client):
    """Test case for get_order_list_light_v3

    Get a paginated list of all Orders without details
    """
    body = openapi_server.OrderListRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/orders/v3/list/light',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

