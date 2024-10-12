# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_members200_response import GetMembers200Response


pytestmark = pytest.mark.asyncio

async def test_get_members(client):
    """Test case for get_members

    List Members
    """
    params = [('page_size', 10),
                    ('order', asc),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v0.2/conversations/{conversation_id}/members'.format(conversation_id='CON-afe887d8-d587-4280-9aae-dfa4c9227d5e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

