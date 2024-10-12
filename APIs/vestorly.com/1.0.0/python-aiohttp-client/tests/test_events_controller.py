# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event_input import EventInput
from openapi_server.models.eventcreateresponse import Eventcreateresponse
from openapi_server.models.eventresponse import Eventresponse
from openapi_server.models.events import Events


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_event(client):
    """Test case for create_event

    
    """
    event = openapi_server.EventInput()
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/events',
        headers=headers,
        json=event,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_event_by_id(client):
    """Test case for find_event_by_id

    
    """
    params = [('access_token', 'access_token_example'),
                    ('vestorly_auth', 'vestorly_auth_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/events/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_events(client):
    """Test case for find_events

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

