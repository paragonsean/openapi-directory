# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_aspsps_ok_body import PostAspspsOKBody
from openapi_server.models.post_aspsps_params_body import PostAspspsParamsBody


pytestmark = pytest.mark.asyncio

async def test_payments_aspsps_post(client):
    """Test case for payments_aspsps_post

    Get list of ASPSPs
    """
    body = openapi_server.PostAspspsParamsBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/openbanking/sandbox/connect/api/payments/aspsps',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

