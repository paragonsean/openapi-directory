# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_account_management_v1_is_email_available_post_request import CustomerAccountManagementV1IsEmailAvailablePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_customer_account_management_v1_is_email_available_post(client):
    """Test case for customer_account_management_v1_is_email_available_post

    customers/isEmailAvailable
    """
    body = openapi_server.CustomerAccountManagementV1IsEmailAvailablePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/customers/isEmailAvailable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

