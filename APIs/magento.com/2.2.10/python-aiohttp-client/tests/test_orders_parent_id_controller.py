# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_order_address_interface import SalesDataOrderAddressInterface
from openapi_server.models.sales_order_address_repository_v1_save_put_request import SalesOrderAddressRepositoryV1SavePutRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_order_address_repository_v1_save_put(client):
    """Test case for sales_order_address_repository_v1_save_put

    orders/{parent_id}
    """
    body = openapi_server.SalesOrderAddressRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/orders/{parent_id}'.format(parent_id='parent_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

