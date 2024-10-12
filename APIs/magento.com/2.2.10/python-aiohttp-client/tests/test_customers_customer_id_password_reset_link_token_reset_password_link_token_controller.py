# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_customer_account_management_v1_validate_reset_password_link_token_get(client):
    """Test case for customer_account_management_v1_validate_reset_password_link_token_get

    customers/{customerId}/password/resetLinkToken/{resetPasswordLinkToken}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/customers/{customer_id}/password/resetLinkToken/{reset_password_link_token}'.format(customer_id=56, reset_password_link_token='reset_password_link_token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

