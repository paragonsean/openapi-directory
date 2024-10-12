# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_creditmemo_management_v1_refund_post_request import SalesCreditmemoManagementV1RefundPostRequest
from openapi_server.models.sales_data_creditmemo_interface import SalesDataCreditmemoInterface


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_creditmemo_management_v1_refund_post(client):
    """Test case for sales_creditmemo_management_v1_refund_post

    creditmemo/refund
    """
    body = openapi_server.SalesCreditmemoManagementV1RefundPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/creditmemo/refund',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

