# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_input_marketing_event_create_request_params import BatchInputMarketingEventCreateRequestParams
from openapi_server.models.batch_input_marketing_event_external_unique_identifier import BatchInputMarketingEventExternalUniqueIdentifier
from openapi_server.models.batch_response_marketing_event_public_default_response import BatchResponseMarketingEventPublicDefaultResponse
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_post_marketing_v3_marketing_events_events_delete_archive(client):
    """Test case for post_marketing_v3_marketing_events_events_delete_archive

    Delete multiple marketing events
    """
    body = {"inputs":[{"externalAccountId":"externalAccountId","externalEventId":"externalEventId","appId":0},{"externalAccountId":"externalAccountId","externalEventId":"externalEventId","appId":0}]}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/marketing/v3/marketing-events/events/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_marketing_v3_marketing_events_events_upsert_do_upsert(client):
    """Test case for post_marketing_v3_marketing_events_events_upsert_do_upsert

    Create or update multiple marketing events
    """
    body = {"inputs":[{"customProperties":[{"sourceId":"sourceId","selectedByUser":True,"sourceLabel":"sourceLabel","persistenceTimestamp":0,"source":"IMPORT","updatedByUserId":5,"sourceMetadata":"sourceMetadata","sourceVid":[1,1],"requestId":"requestId","name":"name","useTimestampAsPersistenceTimestamp":True,"value":"value","selectedByUserTimestamp":6,"isLargeValue":True,"timestamp":5},{"sourceId":"sourceId","selectedByUser":True,"sourceLabel":"sourceLabel","persistenceTimestamp":0,"source":"IMPORT","updatedByUserId":5,"sourceMetadata":"sourceMetadata","sourceVid":[1,1],"requestId":"requestId","name":"name","useTimestampAsPersistenceTimestamp":True,"value":"value","selectedByUserTimestamp":6,"isLargeValue":True,"timestamp":5}],"externalAccountId":"externalAccountId","startDateTime":"2000-01-23T04:56:07.000+00:00","eventCancelled":True,"eventOrganizer":"eventOrganizer","eventUrl":"eventUrl","externalEventId":"externalEventId","eventDescription":"eventDescription","eventName":"eventName","eventType":"eventType","endDateTime":"2000-01-23T04:56:07.000+00:00"},{"customProperties":[{"sourceId":"sourceId","selectedByUser":True,"sourceLabel":"sourceLabel","persistenceTimestamp":0,"source":"IMPORT","updatedByUserId":5,"sourceMetadata":"sourceMetadata","sourceVid":[1,1],"requestId":"requestId","name":"name","useTimestampAsPersistenceTimestamp":True,"value":"value","selectedByUserTimestamp":6,"isLargeValue":True,"timestamp":5},{"sourceId":"sourceId","selectedByUser":True,"sourceLabel":"sourceLabel","persistenceTimestamp":0,"source":"IMPORT","updatedByUserId":5,"sourceMetadata":"sourceMetadata","sourceVid":[1,1],"requestId":"requestId","name":"name","useTimestampAsPersistenceTimestamp":True,"value":"value","selectedByUserTimestamp":6,"isLargeValue":True,"timestamp":5}],"externalAccountId":"externalAccountId","startDateTime":"2000-01-23T04:56:07.000+00:00","eventCancelled":True,"eventOrganizer":"eventOrganizer","eventUrl":"eventUrl","externalEventId":"externalEventId","eventDescription":"eventDescription","eventName":"eventName","eventType":"eventType","endDateTime":"2000-01-23T04:56:07.000+00:00"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/marketing/v3/marketing-events/events/upsert',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

