# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.employee import Employee
from openapi_server.models.employee_info import EmployeeInfo
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_all_employees(client):
    """Test case for get_all_employees

    Get all employees
    """
    params = [('pagesize', 56),
                    ('pagenumber', 56),
                    ('includetotalcount', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/employees'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee(client):
    """Test case for get_employee

    Get employee
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/employees/{employee_id}'.format(company_id='company_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_employee(client):
    """Test case for update_employee

    Update employee
    """
    body = openapi_server.Employee()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/companies/{company_id}/employees/{employee_id}'.format(company_id='company_id_example', employee_id='employee_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

