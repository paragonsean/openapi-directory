# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.search_response import SearchResponse


pytestmark = pytest.mark.asyncio

async def test_web_search(client):
    """Test case for web_search

    The Web Search API lets you send a search query to Bing and get back search results that include links to webpages, images, and more.
    """
    params = [('answerCount', 56),
                    ('cc', 'cc_example'),
                    ('count', 56),
                    ('freshness', 'freshness_example'),
                    ('mkt', 'en-us'),
                    ('offset', 56),
                    ('promote', ['promote_example']),
                    ('q', 'q_example'),
                    ('responseFilter', ['response_filter_example']),
                    ('safeSearch', 'safe_search_example'),
                    ('setLang', 'set_lang_example'),
                    ('textDecorations', True),
                    ('textFormat', 'text_format_example')]
    headers = { 
        'Accept': 'application/json',
        'x_bing_apis_sdk': 'x_bing_apis_sdk_example',
        'accept': 'accept_example',
        'accept_language': 'accept_language_example',
        'pragma': 'pragma_example',
        'user_agent': 'user_agent_example',
        'x_ms_edge_client_id': 'x_ms_edge_client_id_example',
        'x_ms_edge_client_ip': 'x_ms_edge_client_ip_example',
        'x_search_location': 'x_search_location_example',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bing/v7.0/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

