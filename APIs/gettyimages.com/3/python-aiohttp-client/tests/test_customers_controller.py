# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_info_response import CustomerInfoResponse


pytestmark = pytest.mark.asyncio

async def test_v3_customers_current_get(client):
    """Test case for v3_customers_current_get

    Returns information about the current user.
    """
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/customers/current',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

