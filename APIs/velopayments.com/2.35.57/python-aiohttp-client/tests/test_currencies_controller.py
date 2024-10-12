# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.supported_currency_response_v2 import SupportedCurrencyResponseV2


pytestmark = pytest.mark.asyncio

async def test_list_supported_currencies_v2(client):
    """Test case for list_supported_currencies_v2

    List Supported Currencies
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/currencies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

