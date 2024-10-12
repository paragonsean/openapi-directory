# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.retrieve_comments200_response import RetrieveComments200Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_retrieve_comments(client):
    """Test case for retrieve_comments

    Retrieve comments
    """
    params = [('block_id', '{{BLOCK_ID}}'),
                    ('page_size', '100')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'notion_version': '{{NOTION_VERSION}}',
    }
    response = await client.request(
        method='GET',
        path='/v1/comments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

