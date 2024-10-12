# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.media_v1_player_streamer_player_streamer_playback_grant import MediaV1PlayerStreamerPlayerStreamerPlaybackGrant


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_player_streamer_playback_grant(client):
    """Test case for create_player_streamer_playback_grant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'access_control_allow_origin': 'access_control_allow_origin_example',
        'ttl': 56
        }
    response = await client.request(
        method='POST',
        path='/v1/PlayerStreamers/{sid}/PlaybackGrant'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_player_streamer_playback_grant(client):
    """Test case for fetch_player_streamer_playback_grant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/PlayerStreamers/{sid}/PlaybackGrant'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

