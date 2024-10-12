# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.name_type import NameType


pytestmark = pytest.mark.asyncio

async def test_api_name_brand_name_post(client):
    """Test case for api_name_brand_name_post

    Generate brand name suggestions
    """
    params = [('startingWords', 'starting_words_example')]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api/Name/BrandName',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_name_business_name_post(client):
    """Test case for api_name_business_name_post

    Get business names for a specific culture
    """
    params = [('number', 56),
                    ('cultureCode', 'en_US')]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api/Name/BusinessName',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_name_cultures_get(client):
    """Test case for api_name_cultures_get

    Get available cultures
    """
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Name/Cultures',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_name_get(client):
    """Test case for api_name_get

    Get name
    """
    params = [('nameType', openapi_server.NameType()),
                    ('quantity', 56)]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Name',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_name_suggestions_get(client):
    """Test case for api_name_suggestions_get

    Get business name suggestions
    """
    params = [('startingWords', 'starting_words_example')]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/Name/Suggestions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

