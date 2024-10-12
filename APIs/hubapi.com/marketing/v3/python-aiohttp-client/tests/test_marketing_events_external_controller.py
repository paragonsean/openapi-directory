# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.marketing_event_complete_request_params import MarketingEventCompleteRequestParams
from openapi_server.models.marketing_event_default_response import MarketingEventDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_post_marketing_v3_marketing_events_events_external_event_id_complete_complete(client):
    """Test case for post_marketing_v3_marketing_events_events_external_event_id_complete_complete

    
    """
    body = {"startDateTime":"2000-01-23T04:56:07.000+00:00","endDateTime":"2000-01-23T04:56:07.000+00:00"}
    params = [('externalAccountId', 'external_account_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/marketing/v3/marketing-events/events/{external_event_id}/complete'.format(external_event_id='external_event_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

