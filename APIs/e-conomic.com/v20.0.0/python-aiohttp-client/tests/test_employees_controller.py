# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.created_result import CreatedResult
from openapi_server.models.employee import Employee
from openapi_server.models.employee_cursor_results import EmployeeCursorResults
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_employee(client):
    """Test case for create_employee

    Create a single Employee
    """
    body = {"Description":"An awesome employee","Id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v20.0.0/employees',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_employee_by_id(client):
    """Test case for delete_employee_by_id

    Delete single Employee
    """
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v20.0.0/employees/{number}'.format(number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_employees(client):
    """Test case for get_all_employees

    Retrieve all Employees
    """
    params = [('Cursor', 'cursor_example'),
                    ('Filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/employees',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_by_id(client):
    """Test case for get_employee_by_id

    Retrieve single Employee
    """
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/employees/{number}'.format(number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_number_of_employees(client):
    """Test case for get_number_of_employees

    Retrieve the number of Employees
    """
    params = [('Filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/employees/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_page_of_employees(client):
    """Test case for get_page_of_employees

    Retrieve a page of Employees
    """
    params = [('Filter', 'filter_example'),
                    ('Sort', 'sort_example'),
                    ('PageSize', 20),
                    ('SkipPages', 0)]
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/employees/paged',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_employee(client):
    """Test case for update_employee

    Update a single Employee
    """
    body = {"Description":"An awesome employee","Id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v20.0.0/employees',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

