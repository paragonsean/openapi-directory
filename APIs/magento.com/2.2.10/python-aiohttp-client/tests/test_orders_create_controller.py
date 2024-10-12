# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_order_interface import SalesDataOrderInterface
from openapi_server.models.sales_order_repository_v1_save_post_request import SalesOrderRepositoryV1SavePostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_order_repository_v1_save_put(client):
    """Test case for sales_order_repository_v1_save_put

    orders/create
    """
    body = openapi_server.SalesOrderRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/orders/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

