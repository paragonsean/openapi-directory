# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event import Event
from openapi_server.models.position import Position
from openapi_server.models.report_stops import ReportStops
from openapi_server.models.report_summary import ReportSummary
from openapi_server.models.report_trips import ReportTrips


pytestmark = pytest.mark.asyncio

async def test_reports_events_get(client):
    """Test case for reports_events_get

    Fetch a list of Events within the time period for the Devices or Groups
    """
    params = [('deviceId', [56]),
                    ('groupId', [56]),
                    ('type', ['type_example']),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/reports/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_route_get(client):
    """Test case for reports_route_get

    Fetch a list of Positions within the time period for the Devices or Groups
    """
    params = [('deviceId', [56]),
                    ('groupId', [56]),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/reports/route',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_stops_get(client):
    """Test case for reports_stops_get

    Fetch a list of ReportStops within the time period for the Devices or Groups
    """
    params = [('deviceId', [56]),
                    ('groupId', [56]),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/reports/stops',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_summary_get(client):
    """Test case for reports_summary_get

    Fetch a list of ReportSummary within the time period for the Devices or Groups
    """
    params = [('deviceId', [56]),
                    ('groupId', [56]),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/reports/summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_trips_get(client):
    """Test case for reports_trips_get

    Fetch a list of ReportTrips within the time period for the Devices or Groups
    """
    params = [('deviceId', [56]),
                    ('groupId', [56]),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/reports/trips',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

