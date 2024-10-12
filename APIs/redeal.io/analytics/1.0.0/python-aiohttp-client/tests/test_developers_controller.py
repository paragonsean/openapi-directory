# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event_record import EventRecord


pytestmark = pytest.mark.asyncio

async def test_get_events(client):
    """Test case for get_events

    get events for analytics
    """
    params = [('company', 'company_example'),
                    ('site', 'site_example'),
                    ('deal', 'deal_example'),
                    ('type', 'type_example'),
                    ('nexttoken', 'nexttoken_example'),
                    ('queryexecutionid', 'queryexecutionid_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0.0/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

