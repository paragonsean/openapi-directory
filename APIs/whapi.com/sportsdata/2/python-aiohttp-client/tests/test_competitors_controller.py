# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors_wrapper import ErrorsWrapper
from openapi_server.models.event_competitors_wrapper import EventCompetitorsWrapper


pytestmark = pytest.mark.asyncio

async def test_get_event_competitors(client):
    """Test case for get_event_competitors

    Retrieves competitors for a single event by ID.
    """
    params = [('fields', ['fields_example']),
                    ('include', ['include_example']),
                    ('exclude', ['exclude_example'])]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/sportsdata/events/{event_id}/competitors'.format(event_id='event_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

