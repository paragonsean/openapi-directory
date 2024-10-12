# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.free_busy_request import FreeBusyRequest
from openapi_server.models.free_busy_response import FreeBusyResponse


pytestmark = pytest.mark.asyncio

async def test_calendar_freebusy_query(client):
    """Test case for calendar_freebusy_query

    
    """
    body = {"timeMax":"2000-01-23T04:56:07.000+00:00","timeZone":"UTC","calendarExpansionMax":0,"groupExpansionMax":6,"timeMin":"2000-01-23T04:56:07.000+00:00","items":[{"id":"id"},{"id":"id"}]}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/calendar/v3/freeBusy',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

