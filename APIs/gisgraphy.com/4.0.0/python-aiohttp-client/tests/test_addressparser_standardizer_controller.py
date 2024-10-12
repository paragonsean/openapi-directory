# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.address_results_dto import AddressResultsDto


pytestmark = pytest.mark.asyncio

async def test_addressparsing(client):
    """Test case for addressparsing

    split a raw address into several parts
    """
    params = [('address', 'address_example'),
                    ('country', 'country_example'),
                    ('format', XML),
                    ('callback', 'param_callback_example'),
                    ('indent', False),
                    ('standardize', False),
                    ('geocode', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/addressparser/parse',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

