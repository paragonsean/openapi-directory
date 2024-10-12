# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.image_insights import ImageInsights


pytestmark = pytest.mark.asyncio

async def test_images_details(client):
    """Test case for images_details

    The Image Detail Search API lets you search on Bing and get back insights about an image, such as webpages that include the image. This section provides technical details about the query parameters and headers that you use to request insights of images and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Images](https://docs.microsoft.com/azure/cognitive-services/bing-image-search/search-the-web).
    """
    params = [('cab', 3.4),
                    ('cal', 3.4),
                    ('car', 3.4),
                    ('cat', 3.4),
                    ('ct', 'ct_example'),
                    ('cc', 'cc_example'),
                    ('id', 'id_example'),
                    ('imgUrl', 'img_url_example'),
                    ('insightsToken', 'insights_token_example'),
                    ('modules', ['modules_example']),
                    ('mkt', 'mkt_example'),
                    ('q', 'q_example'),
                    ('safeSearch', 'safe_search_example'),
                    ('setLang', 'set_lang_example')]
    headers = { 
        'Accept': 'application/json',
        'x_bing_apis_sdk': 'x_bing_apis_sdk_example',
        'accept': 'accept_example',
        'accept_language': 'accept_language_example',
        'content_type': 'content_type_example',
        'user_agent': 'user_agent_example',
        'x_ms_edge_client_id': 'x_ms_edge_client_id_example',
        'x_ms_edge_client_ip': 'x_ms_edge_client_ip_example',
        'x_search_location': 'x_search_location_example',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bing/v7.0/images/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

