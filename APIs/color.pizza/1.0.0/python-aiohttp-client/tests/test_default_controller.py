# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.get200_response import Get200Response
from openapi_server.models.lists_get200_response import ListsGet200Response
from openapi_server.models.possible_lists import PossibleLists


pytestmark = pytest.mark.asyncio

async def test_lists_get(client):
    """Test case for lists_get

    Get all colors of the default color name list
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/lists/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_names_get(client):
    """Test case for names_get

    Get all colors of the default color name list
    """
    params = [('name', 'name_example'),
                    ('list', openapi_server.PossibleLists())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/names/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_root_get(client):
    """Test case for root_get

    Get all colors of the default color name list
    """
    params = [('list', openapi_server.PossibleLists()),
                    ('values', 'values_example'),
                    ('noduplicates', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_swatch_get(client):
    """Test case for swatch_get

    Generate a color swatch for any color
    """
    params = [('color', 'color_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/swatch/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

