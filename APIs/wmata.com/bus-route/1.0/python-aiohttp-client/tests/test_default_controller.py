# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_call5476362a281d830c946a3d68(client):
    """Test case for call5476362a281d830c946a3d68

    JSON - Bus Position
    """
    params = [('RouteID', 70),
                    ('Lat', 3.4),
                    ('Lon', 3.4),
                    ('Radius', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Bus.svc/json/jBusPositions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476362a281d830c946a3d69(client):
    """Test case for call5476362a281d830c946a3d69

    JSON - Path Details
    """
    params = [('RouteID', 70),
                    ('Date', '_date_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Bus.svc/json/jRouteDetails',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476362a281d830c946a3d6a(client):
    """Test case for call5476362a281d830c946a3d6a

    JSON - Routes
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Bus.svc/json/jRoutes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476362a281d830c946a3d6b(client):
    """Test case for call5476362a281d830c946a3d6b

    JSON - Schedule
    """
    params = [('RouteID', 70),
                    ('Date', '_date_example'),
                    ('IncludingVariations', False)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Bus.svc/json/jRouteSchedule',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476362a281d830c946a3d6c(client):
    """Test case for call5476362a281d830c946a3d6c

    JSON - Schedule at Stop
    """
    params = [('StopID', 1001195),
                    ('Date', '_date_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Bus.svc/json/jStopSchedule',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476362a281d830c946a3d6d(client):
    """Test case for call5476362a281d830c946a3d6d

    JSON - Stop Search
    """
    params = [('Lat', 3.4),
                    ('Lon', 3.4),
                    ('Radius', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Bus.svc/json/jStops',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476362a281d830c946a3d6e(client):
    """Test case for call5476362a281d830c946a3d6e

    XML - Bus Position
    """
    params = [('RouteID', 70),
                    ('Lat', 'lat_example'),
                    ('Lon', 'lon_example'),
                    ('Radius', 'radius_example')]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Bus.svc/BusPositions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476362a281d830c946a3d6f(client):
    """Test case for call5476362a281d830c946a3d6f

    XML - Path Details
    """
    params = [('RouteID', 70),
                    ('Date', '_date_example')]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Bus.svc/RouteDetails',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476362a281d830c946a3d70(client):
    """Test case for call5476362a281d830c946a3d70

    XML - Routes
    """
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Bus.svc/Routes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476362a281d830c946a3d71(client):
    """Test case for call5476362a281d830c946a3d71

    XML - Schedule
    """
    params = [('RouteID', 70),
                    ('Date', '_date_example'),
                    ('IncludingVariations', False)]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Bus.svc/RouteSchedule',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476362a281d830c946a3d72(client):
    """Test case for call5476362a281d830c946a3d72

    XML - Schedule at Stop
    """
    params = [('StopID', 1001195),
                    ('Date', '_date_example')]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Bus.svc/StopSchedule',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476362a281d830c946a3d73(client):
    """Test case for call5476362a281d830c946a3d73

    XML - Stop Search
    """
    params = [('Lat', 'lat_example'),
                    ('Lon', 'lon_example'),
                    ('Radius', 'radius_example')]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Bus.svc/Stops',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

