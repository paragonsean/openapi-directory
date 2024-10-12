# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_price_response import AppPriceResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_app_prices_get_instance(client):
    """Test case for app_prices_get_instance

    
    """
    params = [('fields[appPrices]', ['fields_app_prices_example']),
                    ('include', ['include_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/appPrices/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

