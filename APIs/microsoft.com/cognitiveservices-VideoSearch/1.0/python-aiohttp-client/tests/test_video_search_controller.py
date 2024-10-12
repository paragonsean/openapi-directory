# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.videos import Videos


pytestmark = pytest.mark.asyncio

async def test_videos_search(client):
    """Test case for videos_search

    The Video Search API lets you send a search query to Bing and get back a list of videos that are relevant to the search query. This section provides technical details about the query parameters and headers that you use to request videos and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Videos](https://docs.microsoft.com/azure/cognitive-services/bing-video-search/search-the-web).
    """
    params = [('cc', 'cc_example'),
                    ('count', 56),
                    ('freshness', 'freshness_example'),
                    ('id', 'id_example'),
                    ('length', 'length_example'),
                    ('mkt', 'mkt_example'),
                    ('offset', 56),
                    ('pricing', 'pricing_example'),
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
        path='/bing/v7.0/videos/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

