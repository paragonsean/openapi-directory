# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.priority_entity import PriorityEntity


pytestmark = pytest.mark.asyncio

async def test_get_priorities(client):
    """Test case for get_priorities

    List Priorities
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('path', 'path_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/priorities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

