# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server.models.v3_run_response import V3RunResponse
from openapi_server.models.v3_runs_response import V3RunsResponse


pytestmark = pytest.mark.asyncio

async def test_runs_for_route(client):
    """Test case for runs_for_route

    View all trip/service runs for a specific route ID
    """
    params = [('expand', ['expand_example']),
                    ('date_utc', '2013-10-20T19:20:30+01:00'),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/runs/route/{route_id}'.format(route_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runs_for_route_and_route_type(client):
    """Test case for runs_for_route_and_route_type

    View all trip/service runs for a specific route ID and route type
    """
    params = [('expand', ['expand_example']),
                    ('date_utc', '2013-10-20T19:20:30+01:00'),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/runs/route/{route_id}/route_type/{route_type}'.format(route_id=56, route_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runs_for_run(client):
    """Test case for runs_for_run

    View all trip/service runs for a specific run_ref
    """
    params = [('expand', ['expand_example']),
                    ('date_utc', '2013-10-20T19:20:30+01:00'),
                    ('include_geopath', True),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/runs/{run_ref}'.format(run_ref='run_ref_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runs_for_run_and_route_type(client):
    """Test case for runs_for_run_and_route_type

    View the trip/service run for a specific run_ref and route type
    """
    params = [('expand', ['expand_example']),
                    ('date_utc', '2013-10-20T19:20:30+01:00'),
                    ('include_geopath', True),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/runs/{run_ref}/route_type/{route_type}'.format(run_ref='run_ref_example', route_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

