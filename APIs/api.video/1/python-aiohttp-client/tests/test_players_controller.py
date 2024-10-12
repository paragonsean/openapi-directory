# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.not_found import NotFound
from openapi_server.models.player import Player
from openapi_server.models.player_creation_payload import PlayerCreationPayload
from openapi_server.models.player_update_payload import PlayerUpdatePayload
from openapi_server.models.players_list_response import PlayersListResponse


pytestmark = pytest.mark.asyncio

async def test_d_elete_players_player_id(client):
    """Test case for d_elete_players_player_id

    Delete a player
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/players/{player_id}'.format(player_id='pl45d5vFFGrfdsdsd156dGhh'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_d_elete_players_player_id_logo(client):
    """Test case for d_elete_players_player_id_logo

    Delete logo
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/players/{player_id}/logo'.format(player_id='pl14Db6oMJRH6SRVoOwORacK'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_players(client):
    """Test case for g_et_players

    List all players
    """
    params = [('sortBy', 'createdAt'),
                    ('sortOrder', 'asc'),
                    ('currentPage', 1),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/players',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_players_player_id(client):
    """Test case for g_et_players_player_id

    Show a player
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/players/{player_id}'.format(player_id='pl45d5vFFGrfdsdsd156dGhh'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_atch_players_player_id(client):
    """Test case for p_atch_players_player_id

    Update a player
    """
    body = openapi_server.PlayerUpdatePayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/players/{player_id}'.format(player_id='pl45d5vFFGrfdsdsd156dGhh'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_ost_players(client):
    """Test case for p_ost_players

    Create a player
    """
    body = openapi_server.PlayerCreationPayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/players',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_p_ost_players_player_id_logo(client):
    """Test case for p_ost_players_player_id_logo

    Upload a logo
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('link', 'link_example')
    response = await client.request(
        method='POST',
        path='/players/{player_id}/logo'.format(player_id='pl14Db6oMJRH6SRVoOwORacK'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

