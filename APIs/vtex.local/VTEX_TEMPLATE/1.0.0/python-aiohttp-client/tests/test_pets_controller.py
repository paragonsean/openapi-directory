# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.pet import Pet


pytestmark = pytest.mark.asyncio

async def test_create_pets(client):
    """Test case for create_pets

    Create a pet
    """
    headers = { 
        'Accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pets',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_pets(client):
    """Test case for list_pets

    List all pets
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_pet_by_id(client):
    """Test case for show_pet_by_id

    Info for a specific pet
    """
    headers = { 
        'Accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pets/{pet_id}'.format(pet_id='pet_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

