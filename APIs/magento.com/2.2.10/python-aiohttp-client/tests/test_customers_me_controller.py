# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_customer_repository_v1_save_put_request import CustomerCustomerRepositoryV1SavePutRequest
from openapi_server.models.customer_data_customer_interface import CustomerDataCustomerInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_customer_customer_repository_v1_get_by_id_get(client):
    """Test case for customer_customer_repository_v1_get_by_id_get

    customers/me
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/customers/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_customer_customer_repository_v1_save_put(client):
    """Test case for customer_customer_repository_v1_save_put

    customers/me
    """
    body = openapi_server.CustomerCustomerRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/customers/me',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

