# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_countries_dict_out import GetCountriesDictOut
from openapi_server.models.get_currencies_dict_out import GetCurrenciesDictOut
from openapi_server.models.get_product_types_dict_out import GetProductTypesDictOut


pytestmark = pytest.mark.asyncio

async def test_get_countries_dict(client):
    """Test case for get_countries_dict

    Countries
    """
    params = [('tax_supported', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dictionaries/countries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_currencies_dict(client):
    """Test case for get_currencies_dict

    Currencies
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dictionaries/currencies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_types_dict(client):
    """Test case for get_product_types_dict

    Product types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dictionaries/product_types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

