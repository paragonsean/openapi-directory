# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getcurrencyrate200_response import Getcurrencyrate200Response


pytestmark = pytest.mark.asyncio

async def test_getcurrencyrate(client):
    """Test case for getcurrencyrate

    Gets a foreign currency rate for one US Dollar
    """
    params = [('license', 'license_example'),
                    ('symbol', 'symbol_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getcurrencyrate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

