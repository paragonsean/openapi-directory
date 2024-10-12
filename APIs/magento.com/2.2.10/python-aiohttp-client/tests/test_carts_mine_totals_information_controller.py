# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.checkout_totals_information_management_v1_calculate_post_request import CheckoutTotalsInformationManagementV1CalculatePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_totals_interface import QuoteDataTotalsInterface


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_checkout_totals_information_management_v1_calculate_post(client):
    """Test case for checkout_totals_information_management_v1_calculate_post

    carts/mine/totals-information
    """
    body = openapi_server.CheckoutTotalsInformationManagementV1CalculatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/carts/mine/totals-information',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

