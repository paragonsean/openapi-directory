# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.video_details import VideoDetails


pytestmark = pytest.mark.asyncio

async def test_videos_details(client):
    """Test case for videos_details

    The Video Detail Search API lets you search on Bing and get back insights about a video, such as related videos. This section provides technical details about the query parameters and headers that you use to request insights of videos and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Videos](https://docs.microsoft.com/azure/cognitive-services/bing-video-search/search-the-web).
    """
    params = [('cc', 'cc_example'),
                    ('id', 'id_example'),
                    ('modules', ['modules_example']),
                    ('mkt', 'mkt_example'),
                    ('q', 'q_example'),
                    ('resolution', 'resolution_example'),
                    ('safeSearch', 'safe_search_example'),
                    ('setLang', 'set_lang_example'),
                    ('textDecorations', True),
                    ('textFormat', 'text_format_example')]
    headers = { 
        'Accept': 'application/json',
        'x_bing_apis_sdk': 'x_bing_apis_sdk_example',
        'accept': 'accept_example',
        'accept_language': 'accept_language_example',
        'user_agent': 'user_agent_example',
        'x_ms_edge_client_id': 'x_ms_edge_client_id_example',
        'x_ms_edge_client_ip': 'x_ms_edge_client_ip_example',
        'x_search_location': 'x_search_location_example',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bing/v7.0/videos/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

