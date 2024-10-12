# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.employee_hours_get200_response import EmployeeHoursGet200Response


pytestmark = pytest.mark.asyncio

async def test_employee_hours_get(client):
    """Test case for employee_hours_get

    Used to retrieve details about the logged in user's hours
    """
    params = [('date_from', 'date_from_example'),
                    ('date_to', 'date_to_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/employee_hours',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

