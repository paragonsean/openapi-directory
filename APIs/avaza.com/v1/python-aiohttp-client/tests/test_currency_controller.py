# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.currency_list import CurrencyList


pytestmark = pytest.mark.asyncio

async def test_currency_get(client):
    """Test case for currency_get

    Gets list of Currencies
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Currency',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

