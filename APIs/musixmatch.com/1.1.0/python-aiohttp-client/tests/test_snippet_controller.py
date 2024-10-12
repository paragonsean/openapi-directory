# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.track_snippet_get_get200_response import TrackSnippetGetGet200Response


pytestmark = pytest.mark.asyncio

async def test_track_snippet_get_get(client):
    """Test case for track_snippet_get_get

    
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('track_id', 'track_id_example')]
    headers = { 
        'Accept': 'application/json',
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ws/1.1/track.snippet.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

