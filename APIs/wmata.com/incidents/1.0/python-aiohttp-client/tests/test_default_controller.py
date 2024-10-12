# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_call54763641281d830c946a3d75(client):
    """Test case for call54763641281d830c946a3d75

    JSON - Bus Incidents
    """
    params = [('Route', 'route_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Incidents.svc/json/BusIncidents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call54763641281d830c946a3d76(client):
    """Test case for call54763641281d830c946a3d76

    JSON - Elevator/Escalator Outages
    """
    params = [('StationCode', 'station_code_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Incidents.svc/json/ElevatorIncidents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call54763641281d830c946a3d77(client):
    """Test case for call54763641281d830c946a3d77

    JSON - Rail Incidents
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Incidents.svc/json/Incidents',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call54763641281d830c946a3d78(client):
    """Test case for call54763641281d830c946a3d78

    XML - Bus Incidents
    """
    params = [('Route', 'route_example')]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Incidents.svc/BusIncidents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call54763641281d830c946a3d79(client):
    """Test case for call54763641281d830c946a3d79

    XML - Elevator/Escalator Outages
    """
    params = [('StationCode', 'station_code_example')]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Incidents.svc/ElevatorIncidents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call54763641281d830c946a3d7a(client):
    """Test case for call54763641281d830c946a3d7a

    XML - Rail Incidents
    """
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Incidents.svc/Incidents',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

