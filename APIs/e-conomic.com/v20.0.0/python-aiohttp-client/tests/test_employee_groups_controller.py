# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.created_result import CreatedResult
from openapi_server.models.employee_group import EmployeeGroup
from openapi_server.models.employee_group_cursor_results import EmployeeGroupCursorResults
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_employee_group(client):
    """Test case for create_employee_group

    Create a single Employee group
    """
    body = {"Description":"An awesome employee group","Id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v20.0.0/employeegroups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_employee_group_by_id(client):
    """Test case for delete_employee_group_by_id

    Delete single Employee group
    """
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v20.0.0/employeegroups/{number}'.format(number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_employee_groups(client):
    """Test case for get_all_employee_groups

    Retrieve all Employee groups
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
        path='/api/v20.0.0/employeegroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_group_by_id(client):
    """Test case for get_employee_group_by_id

    Retrieve single Employee group
    """
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/employeegroups/{number}'.format(number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_number_of_employee_groups(client):
    """Test case for get_number_of_employee_groups

    Retrieve the number of Employee groups
    """
    params = [('Filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v20.0.0/employeegroups/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_page_of_employee_groups(client):
    """Test case for get_page_of_employee_groups

    Retrieve a page of Employee groups
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
        path='/api/v20.0.0/employeegroups/paged',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_employee_group(client):
    """Test case for update_employee_group

    Update a single Employee group
    """
    body = {"Description":"An awesome employee group","Id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'X-AgreementGrantToken': 'special-key',
        'X-AppSecretToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v20.0.0/employeegroups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

