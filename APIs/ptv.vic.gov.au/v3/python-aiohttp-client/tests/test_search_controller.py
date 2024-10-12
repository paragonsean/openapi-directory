# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server.models.v3_search_result import V3SearchResult


pytestmark = pytest.mark.asyncio

async def test_search_search(client):
    """Test case for search_search

    View stops, routes and myki ticket outlets that match the search term
    """
    params = [('route_types', [56]),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('max_distance', 3.4),
                    ('include_addresses', True),
                    ('include_outlets', True),
                    ('match_stop_by_suburb', True),
                    ('match_route_by_suburb', True),
                    ('match_stop_by_gtfs_stop_id', True),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/search/{search_term}'.format(search_term='search_term_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

