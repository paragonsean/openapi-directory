# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.events_v1_event_type import EventsV1EventType
from openapi_server.models.list_event_type_response import ListEventTypeResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_event_type(client):
    """Test case for fetch_event_type

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Types/{type}'.format(type='type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_event_type(client):
    """Test case for list_event_type

    
    """
    params = [('SchemaId', 'schema_id_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

