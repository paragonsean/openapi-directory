# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event import Event
from openapi_server.models.manage_event import ManageEvent
from openapi_server.models.problem_detail import ProblemDetail


pytestmark = pytest.mark.asyncio

async def test_story_id_events_get(client):
    """Test case for story_id_events_get

    Events: List Events
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/{id}/events'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_story_id_events_post(client):
    """Test case for story_id_events_post

    Events: Manage Events
    """
    body = openapi_server.ManageEvent()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/story/{id}/events'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

