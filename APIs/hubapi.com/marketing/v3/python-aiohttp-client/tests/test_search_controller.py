# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection_response_marketing_event_external_unique_identifier_no_paging import CollectionResponseMarketingEventExternalUniqueIdentifierNoPaging
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_marketing_v3_marketing_events_events_search_do_search(client):
    """Test case for get_marketing_v3_marketing_events_events_search_do_search

    Search for marketing events
    """
    params = [('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/marketing/v3/marketing-events/events/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

