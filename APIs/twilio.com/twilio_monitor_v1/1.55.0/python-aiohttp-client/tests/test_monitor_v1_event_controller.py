# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_event_response import ListEventResponse
from openapi_server.models.monitor_v1_event import MonitorV1Event


pytestmark = pytest.mark.asyncio

async def test_fetch_event(client):
    """Test case for fetch_event

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Events/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_event(client):
    """Test case for list_event

    
    """
    params = [('ActorSid', 'actor_sid_example'),
                    ('EventType', 'event_type_example'),
                    ('ResourceSid', 'resource_sid_example'),
                    ('SourceIpAddress', 'source_ip_address_example'),
                    ('StartDate', '2013-10-20T19:20:30+01:00'),
                    ('EndDate', '2013-10-20T19:20:30+01:00'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

