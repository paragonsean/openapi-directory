# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.city_list import CityList


pytestmark = pytest.mark.asyncio

async def test_cities_drillers_list(client):
    """Test case for cities_drillers_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/cities/drillers/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cities_installers_list(client):
    """Test case for cities_installers_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/gwells/api/v1/cities/installers/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

