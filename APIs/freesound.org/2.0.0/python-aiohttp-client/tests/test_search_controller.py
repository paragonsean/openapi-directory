# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sound import Sound


pytestmark = pytest.mark.asyncio

async def test_search_text(client):
    """Test case for search_text

    Search sounds
    """
    params = [('query', 'query_example'),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example'),
                    ('group_by_pack', 56),
                    ('page', 1),
                    ('page_size', 15)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/apiv2/search/text',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

