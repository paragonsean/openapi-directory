# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_events200_response import GetEvents200Response


pytestmark = pytest.mark.asyncio

async def test_get_events(client):
    """Test case for get_events

    List Events
    """
    params = [('page_size', 10),
                    ('order', asc),
                    ('cursor', 'cursor_example'),
                    ('start_id', '13'),
                    ('end_id', '19'),
                    ('event_type', 'text')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v0.2/conversations/{conversation_id}/events'.format(conversation_id='CON-afe887d8-d587-4280-9aae-dfa4c9227d5e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

