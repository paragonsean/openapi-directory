# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deleted_game_model import DeletedGameModel
from openapi_server.models.game_endpoints_model import GameEndpointsModel
from openapi_server.models.game_model import GameModel
from openapi_server.models.message_model import MessageModel


pytestmark = pytest.mark.asyncio

async def test_get_games_endpoints_using_get(client):
    """Test case for get_games_endpoints_using_get

    getGamesEndpoints
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/endpoints'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_deleted_using_get(client):
    """Test case for list_deleted_using_get

    listDeleted
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/games/deleted',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_using_get(client):
    """Test case for list_using_get

    list
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/games',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restore_deleted_game_using_post(client):
    """Test case for restore_deleted_game_using_post

    restoreDeletedGame
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/restore'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

