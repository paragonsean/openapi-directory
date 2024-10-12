# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.time_tracking_configuration import TimeTrackingConfiguration
from openapi_server.models.time_tracking_provider import TimeTrackingProvider


pytestmark = pytest.mark.asyncio

async def test_get_available_time_tracking_implementations(client):
    """Test case for get_available_time_tracking_implementations

    Get all time tracking providers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/configuration/timetracking/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_selected_time_tracking_implementation(client):
    """Test case for get_selected_time_tracking_implementation

    Get selected time tracking provider
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/configuration/timetracking',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shared_time_tracking_configuration(client):
    """Test case for get_shared_time_tracking_configuration

    Get time tracking settings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/configuration/timetracking/options',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_select_time_tracking_implementation(client):
    """Test case for select_time_tracking_implementation

    Select time tracking provider
    """
    body = {"name":"name","key":"key","url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/configuration/timetracking',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_shared_time_tracking_configuration(client):
    """Test case for set_shared_time_tracking_configuration

    Set time tracking settings
    """
    body = {"defaultUnit":"minute","workingHoursPerDay":6.027456183070403,"timeFormat":"pretty","workingDaysPerWeek":0.8008281904610115}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/configuration/timetracking/options',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

