# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.marketing_event_create_request_params import MarketingEventCreateRequestParams
from openapi_server.models.marketing_event_default_response import MarketingEventDefaultResponse
from openapi_server.models.marketing_event_public_default_response import MarketingEventPublicDefaultResponse
from openapi_server.models.marketing_event_public_read_response import MarketingEventPublicReadResponse
from openapi_server.models.marketing_event_update_request_params import MarketingEventUpdateRequestParams


pytestmark = pytest.mark.asyncio

async def test_delete_marketing_v3_marketing_events_events_external_event_id_archive(client):
    """Test case for delete_marketing_v3_marketing_events_events_external_event_id_archive

    Delete a marketing event
    """
    params = [('externalAccountId', 'external_account_id_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/marketing/v3/marketing-events/events/{external_event_id}'.format(external_event_id='external_event_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_marketing_v3_marketing_events_events_external_event_id_get_by_id(client):
    """Test case for get_marketing_v3_marketing_events_events_external_event_id_get_by_id

    Get a marketing event
    """
    params = [('externalAccountId', 'external_account_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/marketing/v3/marketing-events/events/{external_event_id}'.format(external_event_id='external_event_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_marketing_v3_marketing_events_events_external_event_id_update(client):
    """Test case for patch_marketing_v3_marketing_events_events_external_event_id_update

    Update a marketing event
    """
    body = {"customProperties":[{"sourceId":"sourceId","selectedByUser":True,"sourceLabel":"sourceLabel","persistenceTimestamp":0,"source":"IMPORT","updatedByUserId":5,"sourceMetadata":"sourceMetadata","sourceVid":[1,1],"requestId":"requestId","name":"name","useTimestampAsPersistenceTimestamp":True,"value":"value","selectedByUserTimestamp":6,"isLargeValue":True,"timestamp":5},{"sourceId":"sourceId","selectedByUser":True,"sourceLabel":"sourceLabel","persistenceTimestamp":0,"source":"IMPORT","updatedByUserId":5,"sourceMetadata":"sourceMetadata","sourceVid":[1,1],"requestId":"requestId","name":"name","useTimestampAsPersistenceTimestamp":True,"value":"value","selectedByUserTimestamp":6,"isLargeValue":True,"timestamp":5}],"startDateTime":"2000-01-23T04:56:07.000+00:00","eventCancelled":True,"eventOrganizer":"eventOrganizer","eventUrl":"eventUrl","eventDescription":"eventDescription","eventName":"eventName","eventType":"eventType","endDateTime":"2000-01-23T04:56:07.000+00:00"}
    params = [('externalAccountId', 'external_account_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/marketing/v3/marketing-events/events/{external_event_id}'.format(external_event_id='external_event_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_marketing_v3_marketing_events_events_create(client):
    """Test case for post_marketing_v3_marketing_events_events_create

    Create a marketing event
    """
    body = {"customProperties":[{"sourceId":"sourceId","selectedByUser":True,"sourceLabel":"sourceLabel","persistenceTimestamp":0,"source":"IMPORT","updatedByUserId":5,"sourceMetadata":"sourceMetadata","sourceVid":[1,1],"requestId":"requestId","name":"name","useTimestampAsPersistenceTimestamp":True,"value":"value","selectedByUserTimestamp":6,"isLargeValue":True,"timestamp":5},{"sourceId":"sourceId","selectedByUser":True,"sourceLabel":"sourceLabel","persistenceTimestamp":0,"source":"IMPORT","updatedByUserId":5,"sourceMetadata":"sourceMetadata","sourceVid":[1,1],"requestId":"requestId","name":"name","useTimestampAsPersistenceTimestamp":True,"value":"value","selectedByUserTimestamp":6,"isLargeValue":True,"timestamp":5}],"externalAccountId":"externalAccountId","startDateTime":"2000-01-23T04:56:07.000+00:00","eventCancelled":True,"eventOrganizer":"eventOrganizer","eventUrl":"eventUrl","externalEventId":"externalEventId","eventDescription":"eventDescription","eventName":"eventName","eventType":"eventType","endDateTime":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/marketing/v3/marketing-events/events',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_marketing_v3_marketing_events_events_external_event_id_cancel_do_cancel(client):
    """Test case for post_marketing_v3_marketing_events_events_external_event_id_cancel_do_cancel

    Mark a marketing event as cancelled
    """
    params = [('externalAccountId', 'external_account_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/marketing/v3/marketing-events/events/{external_event_id}/cancel'.format(external_event_id='external_event_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_marketing_v3_marketing_events_events_external_event_id_replace(client):
    """Test case for put_marketing_v3_marketing_events_events_external_event_id_replace

    Create or update a marketing event
    """
    body = {"customProperties":[{"sourceId":"sourceId","selectedByUser":True,"sourceLabel":"sourceLabel","persistenceTimestamp":0,"source":"IMPORT","updatedByUserId":5,"sourceMetadata":"sourceMetadata","sourceVid":[1,1],"requestId":"requestId","name":"name","useTimestampAsPersistenceTimestamp":True,"value":"value","selectedByUserTimestamp":6,"isLargeValue":True,"timestamp":5},{"sourceId":"sourceId","selectedByUser":True,"sourceLabel":"sourceLabel","persistenceTimestamp":0,"source":"IMPORT","updatedByUserId":5,"sourceMetadata":"sourceMetadata","sourceVid":[1,1],"requestId":"requestId","name":"name","useTimestampAsPersistenceTimestamp":True,"value":"value","selectedByUserTimestamp":6,"isLargeValue":True,"timestamp":5}],"externalAccountId":"externalAccountId","startDateTime":"2000-01-23T04:56:07.000+00:00","eventCancelled":True,"eventOrganizer":"eventOrganizer","eventUrl":"eventUrl","externalEventId":"externalEventId","eventDescription":"eventDescription","eventName":"eventName","eventType":"eventType","endDateTime":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/marketing/v3/marketing-events/events/{external_event_id}'.format(external_event_id='external_event_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

