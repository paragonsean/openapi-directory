# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chaos_parameters import ChaosParameters
from openapi_server.models.chaos_report import ChaosReport
from openapi_server.models.fabric_error import FabricError


pytestmark = pytest.mark.asyncio

async def test_get_chaos_report(client):
    """Test case for get_chaos_report

    Gets the next segment of the Chaos report based on the passed-in continuation token or the passed-in time-range.
    """
    params = [('api-version', 6.0),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('StartTimeUtc', 'start_time_utc_example'),
                    ('EndTimeUtc', 'end_time_utc_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/Chaos/$/Report',
        headers=headers,
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

    Stops Chaos in the cluster if it is already running, otherwise it does nothing.
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

