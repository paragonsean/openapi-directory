# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.matcher_subtitle_get_get200_response import MatcherSubtitleGetGet200Response


pytestmark = pytest.mark.asyncio

async def test_matcher_subtitle_get_get(client):
    """Test case for matcher_subtitle_get_get

    
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('q_track', 'q_track_example'),
                    ('q_artist', 'q_artist_example'),
                    ('f_subtitle_length', 3.4),
                    ('f_subtitle_length_max_deviation', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ws/1.1/matcher.subtitle.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_track_subtitle_get_get(client):
    """Test case for track_subtitle_get_get

    
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
        path='/ws/1.1/track.subtitle.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

