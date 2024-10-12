# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.links_response import LinksResponse


pytestmark = pytest.mark.asyncio

async def test_get_links_links_get(client):
    """Test case for get_links_links_get

    Get Links
    """
    params = [('filter', ''),
                    ('response_format', 'json'),
                    ('email_address', ''),
                    ('response_fields', ''),
                    ('sort', ''),
                    ('page_limit', 20),
                    ('page_offset', 0),
                    ('page_number', 0),
                    ('page_cursor', 0),
                    ('page_above', 0),
                    ('page_below', 0),
                    ('include', 'references'),
                    ('api_hint', '')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/links',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

