# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fleet_fleetname_get200_response import FleetFleetnameGet200Response


pytestmark = pytest.mark.asyncio

async def test_fleet_fleetname_get(client):
    """Test case for fleet_fleetname_get

    Get a Fleet
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/fleet/{fleetname}'.format(fleetname='fleetname_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

