# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_account_management_v1_activate_by_id_put_request import CustomerAccountManagementV1ActivateByIdPutRequest
from openapi_server.models.customer_data_customer_interface import CustomerDataCustomerInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_customer_account_management_v1_activate_put(client):
    """Test case for customer_account_management_v1_activate_put

    customers/{email}/activate
    """
    body = openapi_server.CustomerAccountManagementV1ActivateByIdPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/customers/{email}/activate'.format(email='email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

