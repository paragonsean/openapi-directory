# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.search_response import SearchResponse


pytestmark = pytest.mark.asyncio

async def test_local_search(client):
    """Test case for local_search

    The Local Search API lets you send a search query to Bing and get back search results that include local businesses such as restaurants, hotels, retail stores, or other local businesses. The query can specify the name of the local business or it can ask for a list (for example, restaurants near me).
    """
    params = [('cc', 'cc_example'),
                    ('mkt', 'en-us'),
                    ('q', 'q_example'),
                    ('localcategories', 'localcategories_example'),
                    ('localcircularview', 'localcircularview_example'),
                    ('localmapview', 'localmapview_example'),
                    ('count', 'count_example'),
                    ('first', 'first_example'),
                    ('ResponseFormat', ['response_format_example']),
                    ('SafeSearch', 'safe_search_example'),
                    ('SetLang', 'set_lang_example')]
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
        path='/bing/v7.0/localbusinesses/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

