# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.currencies_currency_id_get200_response import CurrenciesCurrencyIdGet200Response
from openapi_server.models.currencies_get200_response import CurrenciesGet200Response
from openapi_server.models.error_not_found import ErrorNotFound


pytestmark = pytest.mark.asyncio

async def test_currencies_currency_id_get(client):
    """Test case for currencies_currency_id_get

    Get details about one currency
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/currencies/{currency_id}'.format(currency_id='currency_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currencies_get(client):
    """Test case for currencies_get

    Get list of currencies supported in Apacta
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/currencies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

