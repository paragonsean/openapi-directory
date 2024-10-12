# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_response import RestResponse


pytestmark = pytest.mark.asyncio

async def test_counter_using_post(client):
    """Test case for counter_using_post

    Count individuals in streams or collections
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('collectionIds', ['collection_ids_example']),
                    ('streamIds', ['stream_ids_example']),
                    ('startDateTime', '2013-10-20T19:20:30+01:00'),
                    ('endDateTime', '2013-10-20T19:20:30+01:00'),
                    ('visitDuration', 3600000),
                    ('maxIterations', 1),
                    ('maxBatchIterations', 1),
                    ('minNeighborsMergedPerIteration', 5),
                    ('mergingStep', 1.0),
                    ('shuffling', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/v1.1/analytics/counting',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_presence_timeseries_using_post(client):
    """Test case for presence_timeseries_using_post

    Show audience (based on number of occurrences of each person) breakdown per declared attribute (age, gender).
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('streamIds', ['stream_ids_example']),
                    ('startDateTime', '2013-10-20T19:20:30+01:00'),
                    ('endDateTime', '2013-10-20T19:20:30+01:00'),
                    ('step', 3600),
                    ('attributes', ['attributes_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/v1.1/analytics/presence/timeseries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_presence_total_using_post(client):
    """Test case for presence_total_using_post

    Show presence (based on number of occurences of each face) breakdown per declared attribute (age, gender)
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('streamIds', ['stream_ids_example']),
                    ('startDateTime', '2013-10-20T19:20:30+01:00'),
                    ('endDateTime', '2013-10-20T19:20:30+01:00'),
                    ('attributes', ['attributes_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/v1.1/analytics/presence/total',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

