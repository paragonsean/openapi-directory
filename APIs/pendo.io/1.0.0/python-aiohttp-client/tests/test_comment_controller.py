# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comment import Comment


pytestmark = pytest.mark.asyncio

async def test_comments_get(client):
    """Test case for comments_get

    fetch Comment records
    """
    params = [('case_id', 56)]
    headers = { 
        'Accept': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/comments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

