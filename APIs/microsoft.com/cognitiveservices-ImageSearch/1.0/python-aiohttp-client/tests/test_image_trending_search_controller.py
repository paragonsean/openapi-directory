# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.trending_images import TrendingImages


pytestmark = pytest.mark.asyncio

async def test_images_trending(client):
    """Test case for images_trending

    The Image Trending Search API lets you search on Bing and get back a list of images that are trending based on search requests made by others. The images are broken out into different categories. For example, Popular People Searches. For a list of markets that support trending images, see [Trending Images](https://docs.microsoft.com/en-us/azure/cognitive-services/bing-image-search/trending-images).
    """
    params = [('cc', 'cc_example'),
                    ('mkt', 'mkt_example'),
                    ('safeSearch', 'safe_search_example'),
                    ('setLang', 'set_lang_example')]
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
        path='/bing/v7.0/images/trending',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

