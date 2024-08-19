# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.continent_list import ContinentList
from openapi_server.models.country_list import CountryList
from openapi_server.models.currency_list import CurrencyList
from openapi_server.models.language_list import LanguageList
from openapi_server.models.locale import Locale
from openapi_server.models.phone_list import PhoneList


pytestmark = pytest.mark.asyncio

async def test_locale_get(client):
    """Test case for locale_get

    Get User Locale
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locale',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locale_get_continents(client):
    """Test case for locale_get_continents

    List Continents
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locale/continents',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locale_get_countries(client):
    """Test case for locale_get_countries

    List Countries
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locale/countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locale_get_countries_eu(client):
    """Test case for locale_get_countries_eu

    List EU Countries
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locale/countries/eu',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locale_get_countries_phones(client):
    """Test case for locale_get_countries_phones

    List Countries Phone Codes
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locale/countries/phones',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locale_get_currencies(client):
    """Test case for locale_get_currencies

    List Currencies
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locale/currencies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locale_get_languages(client):
    """Test case for locale_get_languages

    List Languages
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locale/languages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

