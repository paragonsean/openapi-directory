# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inbox_registration_entity import InboxRegistrationEntity


pytestmark = pytest.mark.asyncio

async def test_get_inbox_registrations(client):
    """Test case for get_inbox_registrations

    List Inbox Registrations
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('folder_behavior_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/inbox_registrations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

