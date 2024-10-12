# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe330c(client):
    """Test case for call5476364f031f5909e4fe330c

    JSON - Lines
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/json/jLines',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe330d(client):
    """Test case for call5476364f031f5909e4fe330d

    JSON - Parking Information
    """
    params = [('StationCode', 'station_code_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/json/jStationParking',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe330e(client):
    """Test case for call5476364f031f5909e4fe330e

    JSON - Path Between Stations
    """
    params = [('FromStationCode', N06),
                    ('ToStationCode', G05)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/json/jPath',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe330f(client):
    """Test case for call5476364f031f5909e4fe330f

    JSON - Station Entrances
    """
    params = [('Lat', 38.8978168),
                    ('Lon', -77.0404246),
                    ('Radius', 500.0)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/json/jStationEntrances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe3310(client):
    """Test case for call5476364f031f5909e4fe3310

    JSON - Station Information
    """
    params = [('StationCode', A01)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/json/jStationInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe3311(client):
    """Test case for call5476364f031f5909e4fe3311

    JSON - Station List
    """
    params = [('LineCode', 'line_code_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/json/jStations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe3312(client):
    """Test case for call5476364f031f5909e4fe3312

    JSON - Station Timings
    """
    params = [('StationCode', E10)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/json/jStationTimes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe3313(client):
    """Test case for call5476364f031f5909e4fe3313

    JSON - Station to Station Information
    """
    params = [('FromStationCode', E10),
                    ('ToStationCode', J03)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/json/jSrcStationToDstStationInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe3314(client):
    """Test case for call5476364f031f5909e4fe3314

    XML - Lines
    """
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/Lines',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe3315(client):
    """Test case for call5476364f031f5909e4fe3315

    XML - Parking Information
    """
    params = [('StationCode', 'station_code_example')]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/StationParking',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe3316(client):
    """Test case for call5476364f031f5909e4fe3316

    XML - Path Between Stations
    """
    params = [('FromStationCode', N06),
                    ('ToStationCode', G05)]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/Path',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe3317(client):
    """Test case for call5476364f031f5909e4fe3317

    XML - Station Entrances
    """
    params = [('Lat', 38.8978168),
                    ('Lon', -77.0404246),
                    ('Radius', 500.0)]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/StationEntrances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe3318(client):
    """Test case for call5476364f031f5909e4fe3318

    XML - Station Information
    """
    params = [('StationCode', A01)]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/StationInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe3319(client):
    """Test case for call5476364f031f5909e4fe3319

    XML - Station List
    """
    params = [('LineCode', 'line_code_example')]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/Stations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe331a(client):
    """Test case for call5476364f031f5909e4fe331a

    XML - Station Timings
    """
    params = [('StationCode', E10)]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/StationTimes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476364f031f5909e4fe331b(client):
    """Test case for call5476364f031f5909e4fe331b

    XML - Station to Station Information
    """
    params = [('FromStationCode', E10),
                    ('ToStationCode', J03)]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Rail.svc/SrcStationToDstStationInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

