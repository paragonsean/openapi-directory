# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chaos import Chaos
from openapi_server.models.chaos_events_segment import ChaosEventsSegment
from openapi_server.models.chaos_parameters import ChaosParameters
from openapi_server.models.chaos_schedule_description import ChaosScheduleDescription
from openapi_server.models.fabric_error import FabricError


pytestmark = pytest.mark.asyncio

async def test_get_chaos(client):
    """Test case for get_chaos

    Get the status of Chaos.
    """
    params = [('api-version', 6.2),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/Chaos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_chaos_events(client):
    """Test case for get_chaos_events

    Gets the next segment of the Chaos events based on the continuation token or the time range.
    """
    params = [('api-version', 6.2),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('StartTimeUtc', 'start_time_utc_example'),
                    ('EndTimeUtc', 'end_time_utc_example'),
                    ('MaxResults', 0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/Chaos/Events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_chaos_schedule(client):
    """Test case for get_chaos_schedule

    Get the Chaos Schedule defining when and how to run Chaos.
    """
    params = [('api-version', 6.2),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/Chaos/Schedule',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_chaos_schedule(client):
    """Test case for post_chaos_schedule

    Set the schedule used by Chaos.
    """
    chaos_schedule = openapi_server.ChaosScheduleDescription()
    params = [('api-version', 6.2),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Tools/Chaos/Schedule',
        headers=headers,
        json=chaos_schedule,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_start_chaos(client):
    """Test case for start_chaos

    Starts Chaos in the cluster.
    """
    chaos_parameters = openapi_server.ChaosParameters()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Tools/Chaos/$/Start',
        headers=headers,
        json=chaos_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_chaos(client):
    """Test case for stop_chaos

    Stops Chaos if it is running in the cluster and put the Chaos Schedule in a stopped state.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Tools/Chaos/$/Stop',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

