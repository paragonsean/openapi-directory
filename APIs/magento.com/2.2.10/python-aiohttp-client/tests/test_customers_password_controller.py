# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_account_management_v1_initiate_password_reset_put_request import CustomerAccountManagementV1InitiatePasswordResetPutRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_customer_account_management_v1_initiate_password_reset_put(client):
    """Test case for customer_account_management_v1_initiate_password_reset_put

    customers/password
    """
    body = openapi_server.CustomerAccountManagementV1InitiatePasswordResetPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/customers/password',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

