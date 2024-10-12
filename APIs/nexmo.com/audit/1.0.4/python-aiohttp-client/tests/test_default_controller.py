# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.audit_event import AuditEvent
from openapi_server.models.audit_event_types_resp import AuditEventTypesResp
from openapi_server.models.audit_resp import AuditResp
from openapi_server.models.error_forbidden import ErrorForbidden
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_unauthorized import ErrorUnauthorized
from openapi_server.models.event_types import EventTypes
from openapi_server.models.no_content import NoContent


pytestmark = pytest.mark.asyncio

async def test_get_event(client):
    """Test case for get_event

    Retrieve individual audit event
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/beta/audit/events/{id}'.format(id='aaaaaaaa-bbbb-cccc-dddd-0123456789ab'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_events(client):
    """Test case for get_events

    Retrieve audit events
    """
    params = [('event_type', openapi_server.EventTypes()),
                    ('date_from', 'date_from_example'),
                    ('date_to', 'date_to_example'),
                    ('search_text', 'search_text_example'),
                    ('page', 'page_example'),
                    ('size', 30)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/beta/audit/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_events_options(client):
    """Test case for get_events_options

    Retrieve audit event types
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='OPTIONS',
        path='/beta/audit/events',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

