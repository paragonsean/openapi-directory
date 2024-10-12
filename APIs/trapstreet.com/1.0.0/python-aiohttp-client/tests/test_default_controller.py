# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.address_get200_response import AddressGet200Response


pytestmark = pytest.mark.asyncio

async def test_address_get(client):
    """Test case for address_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/{address}'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

