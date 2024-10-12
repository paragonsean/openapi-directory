# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pause_watching_in_a_media_center_request import PauseWatchingInAMediaCenterRequest
from openapi_server.models.start_watching_in_a_media_center_request import StartWatchingInAMediaCenterRequest
from openapi_server.models.stop_or_finish_watching_in_a_media_center_request import StopOrFinishWatchingInAMediaCenterRequest


pytestmark = pytest.mark.asyncio

async def test_pause_watching_in_a_media_center(client):
    """Test case for pause_watching_in_a_media_center

    Pause watching in a media center
    """
    body = openapi_server.PauseWatchingInAMediaCenterRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/scrobble/pause',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_watching_in_a_media_center(client):
    """Test case for start_watching_in_a_media_center

    Start watching in a media center
    """
    body = openapi_server.StartWatchingInAMediaCenterRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/scrobble/start',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_or_finish_watching_in_a_media_center(client):
    """Test case for stop_or_finish_watching_in_a_media_center

    Stop or finish watching in a media center
    """
    body = openapi_server.StopOrFinishWatchingInAMediaCenterRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/scrobble/stop',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

