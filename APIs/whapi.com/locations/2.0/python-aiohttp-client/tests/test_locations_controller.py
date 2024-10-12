# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.addresses import Addresses
from openapi_server.models.countries import Countries
from openapi_server.models.country import Country
from openapi_server.models.currencies import Currencies
from openapi_server.models.currency import Currency
from openapi_server.models.locations_errors import LocationsErrors


pytestmark = pytest.mark.asyncio

async def test_address_lookup(client):
    """Test case for address_lookup

    
    """
    params = [('houseNum', 'house_num_example'),
                    ('postCode', 'post_code_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/address/lookup/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_countries(client):
    """Test case for get_countries

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/countries/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_country(client):
    """Test case for get_country

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/countries/{country_code}'.format(country_code='country_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_currencies(client):
    """Test case for get_currencies

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/currencies/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_currency(client):
    """Test case for get_currency

    
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/currencies/{currency_code}'.format(currency_code='currency_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

