# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event_enum_twilio_edge import EventEnumTwilioEdge
from openapi_server.models.list_event_response import ListEventResponse


pytestmark = pytest.mark.asyncio

async def test_list_event(client):
    """Test case for list_event

    
    """
    params = [('Edge', openapi_server.EventEnumTwilioEdge()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Voice/{call_sid}/Events'.format(call_sid='call_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

