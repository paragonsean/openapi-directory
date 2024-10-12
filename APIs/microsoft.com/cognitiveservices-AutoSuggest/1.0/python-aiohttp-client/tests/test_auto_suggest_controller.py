# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.suggestions import Suggestions


pytestmark = pytest.mark.asyncio

async def test_auto_suggest(client):
    """Test case for auto_suggest

    The AutoSuggest API lets you send a search query to Bing and get back a list of query suggestions. This section provides technical details about the query parameters and headers that you use to request suggestions and the JSON response objects that contain them.
    """
    params = [('cc', 'cc_example'),
                    ('mkt', 'en-us'),
                    ('q', 'q_example'),
                    ('safeSearch', 'safe_search_example'),
                    ('setLang', 'set_lang_example'),
                    ('ResponseFormat', ['response_format_example'])]
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
        path='/bing/v7.0/Suggestions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

