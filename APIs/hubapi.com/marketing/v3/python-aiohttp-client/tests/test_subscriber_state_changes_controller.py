# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_input_marketing_event_email_subscriber import BatchInputMarketingEventEmailSubscriber
from openapi_server.models.batch_input_marketing_event_subscriber import BatchInputMarketingEventSubscriber
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_post_marketing_v3_marketing_events_events_external_event_id_subscriber_state_email_upsert_do_email_upsert_by_id(client):
    """Test case for post_marketing_v3_marketing_events_events_external_event_id_subscriber_state_email_upsert_do_email_upsert_by_id

    Record
    """
    body = {"inputs":[{"contactProperties":{"key":"contactProperties"},"email":"email","properties":{"key":"properties"},"interactionDateTime":0},{"contactProperties":{"key":"contactProperties"},"email":"email","properties":{"key":"properties"},"interactionDateTime":0}]}
    params = [('externalAccountId', 'external_account_id_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/marketing/v3/marketing-events/events/{external_event_id}/{subscriber_state}/email-upsert'.format(external_event_id='external_event_id_example', subscriber_state='subscriber_state_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_marketing_v3_marketing_events_events_external_event_id_subscriber_state_upsert_do_upsert_by_id(client):
    """Test case for post_marketing_v3_marketing_events_events_external_event_id_subscriber_state_upsert_do_upsert_by_id

    Record
    """
    body = {"inputs":[{"vid":6,"properties":{"key":"properties"},"interactionDateTime":0},{"vid":6,"properties":{"key":"properties"},"interactionDateTime":0}]}
    params = [('externalAccountId', 'external_account_id_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/marketing/v3/marketing-events/events/{external_event_id}/{subscriber_state}/upsert'.format(external_event_id='external_event_id_example', subscriber_state='subscriber_state_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

