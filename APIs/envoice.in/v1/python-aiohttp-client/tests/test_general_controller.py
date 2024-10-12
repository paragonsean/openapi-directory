# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.country_details_api_model import CountryDetailsApiModel
from openapi_server.models.currency_details_api_model import CurrencyDetailsApiModel
from openapi_server.models.ui_language_details_api_model import UILanguageDetailsApiModel


pytestmark = pytest.mark.asyncio

async def test_general_api_countries(client):
    """Test case for general_api_countries

    Return all of the platform supported countries
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/general/countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_general_api_currencies(client):
    """Test case for general_api_currencies

    Return all of the platform supported currencies
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/general/currencies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_general_api_date_formats(client):
    """Test case for general_api_date_formats

    Return all of the platform supported Date Formats
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/general/dateformats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_general_api_ui_languages(client):
    """Test case for general_api_ui_languages

    Return all of the platform supported UI languages
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/general/uilanguages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

