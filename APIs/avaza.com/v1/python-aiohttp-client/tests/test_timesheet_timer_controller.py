# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_timesheet_timer_get_running_timer(client):
    """Test case for timesheet_timer_get_running_timer

    Gets the  Running Timer if there is one for a user.
    """
    params = [('UserID', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/TimesheetTimer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timesheet_timer_start_timer(client):
    """Test case for timesheet_timer_start_timer

    Starts a Timer running on an existing Timesheet Entry
    """
    params = [('UserID', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/TimesheetTimer/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timesheet_timer_stop_timer(client):
    """Test case for timesheet_timer_stop_timer

    Stop the timer running on an existing Timesheet Entry
    """
    params = [('UserID', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/TimesheetTimer/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

