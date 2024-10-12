# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

async def test_search_messages(client):
    """Test case for search_messages

    
    """
    params = [('token', 'token_example'),
                    ('count', 56),
                    ('highlight', True),
                    ('page', 56),
                    ('query', 'query_example'),
                    ('sort', 'sort_example'),
                    ('sort_dir', 'sort_dir_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/search.messages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

