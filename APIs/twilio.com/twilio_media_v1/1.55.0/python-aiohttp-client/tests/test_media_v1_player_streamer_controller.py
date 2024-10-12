# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_player_streamer_response import ListPlayerStreamerResponse
from openapi_server.models.media_v1_player_streamer import MediaV1PlayerStreamer
from openapi_server.models.player_streamer_enum_order import PlayerStreamerEnumOrder
from openapi_server.models.player_streamer_enum_status import PlayerStreamerEnumStatus
from openapi_server.models.player_streamer_enum_update_status import PlayerStreamerEnumUpdateStatus


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_player_streamer(client):
    """Test case for create_player_streamer

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'max_duration': 56,
        'status_callback': 'status_callback_example',
        'status_callback_method': 'status_callback_method_example',
        'video': True
        }
    response = await client.request(
        method='POST',
        path='/v1/PlayerStreamers',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_player_streamer(client):
    """Test case for fetch_player_streamer

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/PlayerStreamers/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_player_streamer(client):
    """Test case for list_player_streamer

    
    """
    params = [('Order', openapi_server.PlayerStreamerEnumOrder()),
                    ('Status', openapi_server.PlayerStreamerEnumStatus()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/PlayerStreamers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_player_streamer(client):
    """Test case for update_player_streamer

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'status': openapi_server.PlayerStreamerEnumUpdateStatus()
        }
    response = await client.request(
        method='POST',
        path='/v1/PlayerStreamers/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

