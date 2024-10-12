# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.search_response import SearchResponse


pytestmark = pytest.mark.asyncio

async def test_custom_instance_search(client):
    """Test case for custom_instance_search

    The Custom Search API lets you send a search query to Bing and get back web pages found in your custom view of the web.
    """
    params = [('customConfig', 'custom_config_example'),
                    ('cc', 'cc_example'),
                    ('count', 56),
                    ('mkt', 'en-us'),
                    ('offset', 56),
                    ('q', 'q_example'),
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
        path='/bingcustomsearch/v7.0/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

