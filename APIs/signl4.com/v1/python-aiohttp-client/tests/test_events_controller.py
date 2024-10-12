# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.event_filter import EventFilter
from openapi_server.models.event_parameter_info import EventParameterInfo
from openapi_server.models.overview_event import OverviewEvent
from openapi_server.models.overview_event_paged_results_public import OverviewEventPagedResultsPublic


pytestmark = pytest.mark.asyncio

async def test_events_event_id_overview_get(client):
    """Test case for events_event_id_overview_get

    Get overview event
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/events/{event_id}/overview'.format(event_id='event_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_event_id_parameters_get(client):
    """Test case for events_event_id_parameters_get

    Get event parameters
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/events/{event_id}/parameters'.format(event_id='event_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_events_paged_post(client):
    """Test case for events_paged_post

    Get overview event paged.
    """
    body = {"minCreationDate":"2000-01-23T04:56:07.000+00:00","modifiedSince":"2000-01-23T04:56:07.000+00:00","teamId":"teamId","eventStatusCode":0,"maxCreationDate":"2000-01-23T04:56:07.000+00:00","textToSearch":"textToSearch","continuationToken":{"nextTableName":"nextTableName","nextRowKey":"nextRowKey","nextPartitionKey":"nextPartitionKey"}}
    params = [('maxResults', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/events/paged',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

