# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getaddressmatch200_response import Getaddressmatch200Response


pytestmark = pytest.mark.asyncio

async def test_getaddressmatch(client):
    """Test case for getaddressmatch

    Gets a similarity key for matching purposes for address data
    """
    params = [('license', 'license_example'),
                    ('address', 'address_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getaddressmatch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

