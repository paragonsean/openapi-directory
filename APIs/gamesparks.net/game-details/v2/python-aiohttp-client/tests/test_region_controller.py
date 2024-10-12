# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.game_region_options_dto import GameRegionOptionsDTO
from openapi_server.models.message_model import MessageModel
from openapi_server.models.region_result import RegionResult


pytestmark = pytest.mark.asyncio

async def test_get_game_region_options_using_get(client):
    """Test case for get_game_region_options_using_get

    getGameRegionOptions
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{game_api_key}/regions'.format(game_api_key='game_api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_region_options_using_get(client):
    """Test case for get_region_options_using_get

    getRegionOptions
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/regions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_game_region_using_post(client):
    """Test case for set_game_region_using_post

    setGameRegion
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{game_api_key}/region/{region_code}'.format(game_api_key='game_api_key_example', region_code='region_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

