# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_account_management_v1_validate_put_request import CustomerAccountManagementV1ValidatePutRequest
from openapi_server.models.customer_data_validation_results_interface import CustomerDataValidationResultsInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_customer_account_management_v1_validate_put(client):
    """Test case for customer_account_management_v1_validate_put

    customers/validate
    """
    body = openapi_server.CustomerAccountManagementV1ValidatePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/customers/validate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

