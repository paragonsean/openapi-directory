# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.spot import Spot


pytestmark = pytest.mark.asyncio

async def test_api_v2_spots_get(client):
    """Test case for api_v2_spots_get

    Returns the spots matching the query parameters.
    """
    params = [('pageStart', 0),
                    ('pageSize', 500),
                    ('orderById', 'order_by_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/spots',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_spots_id_delete(client):
    """Test case for api_v2_spots_id_delete

    Deletes the spot with the given ID.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/spots/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_spots_id_get(client):
    """Test case for api_v2_spots_id_get

    Returns the spot matching the given ID.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/spots/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_api_v2_spots_post(client):
    """Test case for api_v2_spots_post

    Creates a new spot.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'cd_drive_uri': 'cd_drive_uri_example',
        'name': 'name_example',
        'notes': 'notes_example'
        }
    response = await client.request(
        method='POST',
        path='/api/v2/spots',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

