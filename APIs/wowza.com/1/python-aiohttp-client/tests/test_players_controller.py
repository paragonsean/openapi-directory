# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_player_url200_response import CreatePlayerUrl200Response
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error410 import Error410
from openapi_server.models.error422 import Error422
from openapi_server.models.player_update_input import PlayerUpdateInput
from openapi_server.models.players import Players
from openapi_server.models.request_player_rebuild200_response import RequestPlayerRebuild200Response
from openapi_server.models.show_player200_response import ShowPlayer200Response
from openapi_server.models.show_player_state200_response import ShowPlayerState200Response
from openapi_server.models.url_create_input import UrlCreateInput
from openapi_server.models.url_update_input import UrlUpdateInput
from openapi_server.models.urls import Urls


pytestmark = pytest.mark.asyncio

async def test_create_player_url(client):
    """Test case for create_player_url

    Create a player URL
    """
    url = openapi_server.UrlCreateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/players/{player_id}/urls'.format(player_id='player_id_example'),
        headers=headers,
        json=url,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_player_url(client):
    """Test case for delete_player_url

    Delete a player URL
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/players/{player_id}/urls/{id}'.format(player_id='player_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_player_urls(client):
    """Test case for list_player_urls

    Fetch all player URLs
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/players/{player_id}/urls'.format(player_id='player_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_players(client):
    """Test case for list_players

    Fetch all players
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/players',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_player_rebuild(client):
    """Test case for request_player_rebuild

    Rebuild player code
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/players/{id}/rebuild'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_player(client):
    """Test case for show_player

    Fetch a player
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/players/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_player_state(client):
    """Test case for show_player_state

    Fetch the state of a player
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/players/{id}/state'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_player_url(client):
    """Test case for show_player_url

    Fetch a player URL
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/players/{player_id}/urls/{id}'.format(player_id='player_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_player(client):
    """Test case for update_player

    Update a player
    """
    player = openapi_server.PlayerUpdateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/players/{id}'.format(id='id_example'),
        headers=headers,
        json=player,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_player_url(client):
    """Test case for update_player_url

    Update a player URL
    """
    url = openapi_server.UrlUpdateInput()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/players/{player_id}/urls/{id}'.format(player_id='player_id_example', id='id_example'),
        headers=headers,
        json=url,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

