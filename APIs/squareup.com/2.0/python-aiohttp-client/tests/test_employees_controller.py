# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_employees_response import ListEmployeesResponse
from openapi_server.models.retrieve_employee_response import RetrieveEmployeeResponse


pytestmark = pytest.mark.asyncio

async def test_v2_employees_get(client):
    """Test case for v2_employees_get

    ListEmployees
    """
    params = [('location_id', 'location_id_example'),
                    ('status', 'status_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/employees',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_employees_id_get(client):
    """Test case for v2_employees_id_get

    RetrieveEmployee
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/employees/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

