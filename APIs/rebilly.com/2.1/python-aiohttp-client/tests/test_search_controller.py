# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.search import Search


pytestmark = pytest.mark.asyncio

async def test_get_search(client):
    """Test case for get_search

    Search merchant data
    """
    params = [('sort', ['sort_example']),
                    ('limit', 56),
                    ('offset', 56),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

