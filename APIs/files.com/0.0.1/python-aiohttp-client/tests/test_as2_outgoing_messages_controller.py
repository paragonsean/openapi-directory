# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.as2_outgoing_message_entity import As2OutgoingMessageEntity


pytestmark = pytest.mark.asyncio

async def test_get_as2_outgoing_messages(client):
    """Test case for get_as2_outgoing_messages

    List As2 Outgoing Messages
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_gt', None),
                    ('filter_gteq', None),
                    ('filter_lt', None),
                    ('filter_lteq', None),
                    ('as2_partner_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/as2_outgoing_messages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

