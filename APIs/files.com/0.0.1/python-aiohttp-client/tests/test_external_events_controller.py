# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.external_event_entity import ExternalEventEntity


pytestmark = pytest.mark.asyncio

async def test_get_external_events(client):
    """Test case for get_external_events

    List External Events
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_gt', None),
                    ('filter_gteq', None),
                    ('filter_prefix', None),
                    ('filter_lt', None),
                    ('filter_lteq', None)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/external_events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_external_events_id(client):
    """Test case for get_external_events_id

    Show External Event
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/external_events/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_external_events(client):
    """Test case for post_external_events

    Create External Event
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('body', 'body_example')
    data.add_field('status', 'status_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/external_events',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

