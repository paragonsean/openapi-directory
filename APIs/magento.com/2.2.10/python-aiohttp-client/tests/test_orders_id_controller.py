# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_order_interface import SalesDataOrderInterface


pytestmark = pytest.mark.asyncio

async def test_sales_order_repository_v1_get_get(client):
    """Test case for sales_order_repository_v1_get_get

    orders/{id}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/orders/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

