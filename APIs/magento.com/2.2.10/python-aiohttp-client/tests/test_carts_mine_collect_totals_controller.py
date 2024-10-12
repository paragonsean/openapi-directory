# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_total_management_v1_collect_totals_put_request import QuoteCartTotalManagementV1CollectTotalsPutRequest
from openapi_server.models.quote_data_totals_interface import QuoteDataTotalsInterface


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_quote_cart_total_management_v1_collect_totals_put(client):
    """Test case for quote_cart_total_management_v1_collect_totals_put

    carts/mine/collect-totals
    """
    body = openapi_server.QuoteCartTotalManagementV1CollectTotalsPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/carts/mine/collect-totals',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

