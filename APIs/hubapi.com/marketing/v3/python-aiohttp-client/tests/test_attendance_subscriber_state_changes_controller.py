# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_input_marketing_event_email_subscriber import BatchInputMarketingEventEmailSubscriber
from openapi_server.models.batch_input_marketing_event_subscriber import BatchInputMarketingEventSubscriber
from openapi_server.models.batch_response_subscriber_email_response import BatchResponseSubscriberEmailResponse
from openapi_server.models.batch_response_subscriber_vid_response import BatchResponseSubscriberVidResponse
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_post_marketing_v3_marketing_events_attendance_external_event_id_subscriber_state_create_create(client):
    """Test case for post_marketing_v3_marketing_events_attendance_external_event_id_subscriber_state_create_create

    Record
    """
    body = {"inputs":[{"vid":6,"properties":{"key":"properties"},"interactionDateTime":0},{"vid":6,"properties":{"key":"properties"},"interactionDateTime":0}]}
    params = [('externalAccountId', 'external_account_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/marketing/v3/marketing-events/attendance/{external_event_id}/{subscriber_state}/create'.format(external_event_id='external_event_id_example', subscriber_state='subscriber_state_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_marketing_v3_marketing_events_attendance_external_event_id_subscriber_state_email_create_create_by_email(client):
    """Test case for post_marketing_v3_marketing_events_attendance_external_event_id_subscriber_state_email_create_create_by_email

    Record
    """
    body = {"inputs":[{"contactProperties":{"key":"contactProperties"},"email":"email","properties":{"key":"properties"},"interactionDateTime":0},{"contactProperties":{"key":"contactProperties"},"email":"email","properties":{"key":"properties"},"interactionDateTime":0}]}
    params = [('externalAccountId', 'external_account_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/marketing/v3/marketing-events/attendance/{external_event_id}/{subscriber_state}/email-create'.format(external_event_id='external_event_id_example', subscriber_state='subscriber_state_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

