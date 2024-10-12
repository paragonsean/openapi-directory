# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_sales_shipment_management_v1_notify_post(client):
    """Test case for sales_shipment_management_v1_notify_post

    shipment/{id}/emails
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/shipment/{id}/emails'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

