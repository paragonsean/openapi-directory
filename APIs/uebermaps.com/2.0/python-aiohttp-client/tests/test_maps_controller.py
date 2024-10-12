# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.map import Map
from openapi_server.models.map_editable import MapEditable
from openapi_server.models.map_with_relation import MapWithRelation


pytestmark = pytest.mark.asyncio

async def test_maps_get(client):
    """Test case for maps_get

    List your own maps
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/maps',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maps_id_delete(client):
    """Test case for maps_id_delete

    Delete map
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/maps/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maps_id_get(client):
    """Test case for maps_id_get

    Get map
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/maps/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maps_id_patch(client):
    """Test case for maps_id_patch

    Update map
    """
    map = {"map_settings":{"respotting_to_this_map":True,"visitor_access":"","editor_access":""},"visibility":"public","description":"A collection of restaurants, cafes, clubs and random spots that I recommend in Berlin","title":"My favourite places in Berlin","picture":"<BASE_64_ENCODED_STRING>"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/maps/{id}'.format(id=56),
        headers=headers,
        json=map,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maps_post(client):
    """Test case for maps_post

    Create map
    """
    map = {"map_settings":{"respotting_to_this_map":True,"visitor_access":"","editor_access":""},"visibility":"public","description":"A collection of restaurants, cafes, clubs and random spots that I recommend in Berlin","title":"My favourite places in Berlin","picture":"<BASE_64_ENCODED_STRING>"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/maps',
        headers=headers,
        json=map,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_maps_get(client):
    """Test case for users_user_id_maps_get

    List maps for a given user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/users/{user_id}/maps'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

