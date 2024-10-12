# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.images import Images


pytestmark = pytest.mark.asyncio

async def test_images_search(client):
    """Test case for images_search

    The Image Search API lets you send a search query to Bing and get back a list of relevant images. This section provides technical details about the query parameters and headers that you use to request images and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Images](https://docs.microsoft.com/azure/cognitive-services/bing-image-search/search-the-web).
    """
    params = [('aspect', 'aspect_example'),
                    ('color', 'color_example'),
                    ('cc', 'cc_example'),
                    ('count', 56),
                    ('freshness', 'freshness_example'),
                    ('height', 56),
                    ('id', 'id_example'),
                    ('imageContent', 'image_content_example'),
                    ('imageType', 'image_type_example'),
                    ('license', 'license_example'),
                    ('mkt', 'mkt_example'),
                    ('maxFileSize', 56),
                    ('maxHeight', 56),
                    ('maxWidth', 56),
                    ('minFileSize', 56),
                    ('minHeight', 56),
                    ('minWidth', 56),
                    ('offset', 56),
                    ('q', 'q_example'),
                    ('safeSearch', 'safe_search_example'),
                    ('size', 'size_example'),
                    ('setLang', 'set_lang_example'),
                    ('width', 56)]
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
        path='/bing/v7.0/images/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

