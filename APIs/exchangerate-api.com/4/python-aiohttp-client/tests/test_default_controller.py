# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.latest_base_currency_get200_response import LatestBaseCurrencyGet200Response
from openapi_server.models.latest_base_currency_get404_response import LatestBaseCurrencyGet404Response


pytestmark = pytest.mark.asyncio

async def test_latest_base_currency_get(client):
    """Test case for latest_base_currency_get

    Returns latest exchange rates in parameter-supplied base currency.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v4/latest/{base_currency}'.format(base_currency='base_currency_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

