# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_customer_repository_v1_save_put_request import CustomerCustomerRepositoryV1SavePutRequest
from openapi_server.models.customer_data_customer_interface import CustomerDataCustomerInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_customer_customer_repository_v1_delete_by_id_delete(client):
    """Test case for customer_customer_repository_v1_delete_by_id_delete

    customers/{customerId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/customers/{customer_id}'.format(customer_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_customers_customer_id_get(client):
    """Test case for v1_customers_customer_id_get

    customers/{customerId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/customers/{customer_id}'.format(customer_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v1_customers_customer_id_put(client):
    """Test case for v1_customers_customer_id_put

    customers/{customerId}
    """
    body = openapi_server.CustomerCustomerRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/customers/{customer_id}'.format(customer_id='customer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

