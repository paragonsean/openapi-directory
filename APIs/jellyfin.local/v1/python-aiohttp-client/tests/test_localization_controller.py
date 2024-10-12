# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.country_info import CountryInfo
from openapi_server.models.culture_dto import CultureDto
from openapi_server.models.localization_option import LocalizationOption
from openapi_server.models.parental_rating import ParentalRating


pytestmark = pytest.mark.asyncio

async def test_get_countries(client):
    """Test case for get_countries

    Gets known countries.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Localization/Countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cultures(client):
    """Test case for get_cultures

    Gets known cultures.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Localization/Cultures',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_localization_options(client):
    """Test case for get_localization_options

    Gets localization options.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Localization/Options',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_parental_ratings(client):
    """Test case for get_parental_ratings

    Gets known parental ratings.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Localization/ParentalRatings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

