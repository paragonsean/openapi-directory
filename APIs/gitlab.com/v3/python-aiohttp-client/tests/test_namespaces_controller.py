# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.namespace import Namespace


pytestmark = pytest.mark.asyncio

async def test_get_v3_namespaces(client):
    """Test case for get_v3_namespaces

    Get a namespaces list
    """
    params = [('search', 'search_example'),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/namespaces',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

