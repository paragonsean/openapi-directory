# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v3_disruption_modes_response import V3DisruptionModesResponse
from openapi_server.models.v3_disruption_response import V3DisruptionResponse
from openapi_server.models.v3_disruptions_response import V3DisruptionsResponse
from openapi_server.models.v3_error_response import V3ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_disruptions_get_all_disruptions(client):
    """Test case for disruptions_get_all_disruptions

    View all disruptions for all route types
    """
    params = [('route_types', [56]),
                    ('disruption_modes', [56]),
                    ('disruption_status', 'disruption_status_example'),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/disruptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disruptions_get_disruption_by_id(client):
    """Test case for disruptions_get_disruption_by_id

    View a specific disruption
    """
    params = [('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/disruptions/{disruption_id}'.format(disruption_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disruptions_get_disruption_modes(client):
    """Test case for disruptions_get_disruption_modes

    Get all disruption modes
    """
    params = [('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/disruptions/modes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disruptions_get_disruptions_by_route(client):
    """Test case for disruptions_get_disruptions_by_route

    View all disruptions for a particular route
    """
    params = [('disruption_status', 'disruption_status_example'),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/disruptions/route/{route_id}'.format(route_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disruptions_get_disruptions_by_route_and_stop(client):
    """Test case for disruptions_get_disruptions_by_route_and_stop

    View all disruptions for a particular route and stop
    """
    params = [('disruption_status', 'disruption_status_example'),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/disruptions/route/{route_id}/stop/{stop_id}'.format(route_id=56, stop_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disruptions_get_disruptions_by_stop(client):
    """Test case for disruptions_get_disruptions_by_stop

    View all disruptions for a particular stop
    """
    params = [('disruption_status', 'disruption_status_example'),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/disruptions/stop/{stop_id}'.format(stop_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

