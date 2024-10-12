# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.address_results_dto import AddressResultsDto


pytestmark = pytest.mark.asyncio

async def test_reversegeocode(client):
    """Test case for reversegeocode

    Reverse geocode an address
    """
    params = [('lat', 3.4),
                    ('lng', 3.4),
                    ('format', XML),
                    ('from', 1),
                    ('to', 10),
                    ('callback', 'param_callback_example'),
                    ('indent', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/reversegeocoding/reversegeocode',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

