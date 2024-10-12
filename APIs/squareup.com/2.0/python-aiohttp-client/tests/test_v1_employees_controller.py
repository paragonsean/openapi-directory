# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v1_employee import V1Employee
from openapi_server.models.v1_employee_role import V1EmployeeRole


pytestmark = pytest.mark.asyncio

async def test_create_employee(client):
    """Test case for create_employee

    CreateEmployee
    """
    body = {"updated_at":"updated_at","created_at":"created_at","last_name":"last_name","external_id":"external_id","id":"id","first_name":"first_name","email":"email","role_ids":["role_ids","role_ids"],"authorized_location_ids":["authorized_location_ids","authorized_location_ids"],"status":"status"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/me/employees',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_employee_role(client):
    """Test case for create_employee_role

    CreateEmployeeRole
    """
    body = {"updated_at":"updated_at","is_owner":True,"permissions":["permissions","permissions"],"name":"name","created_at":"created_at","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/me/roles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_employee_roles(client):
    """Test case for list_employee_roles

    ListEmployeeRoles
    """
    params = [('order', 'order_example'),
                    ('limit', 56),
                    ('batch_token', 'batch_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/roles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_employees(client):
    """Test case for list_employees

    ListEmployees
    """
    params = [('order', 'order_example'),
                    ('begin_updated_at', 'begin_updated_at_example'),
                    ('end_updated_at', 'end_updated_at_example'),
                    ('begin_created_at', 'begin_created_at_example'),
                    ('end_created_at', 'end_created_at_example'),
                    ('status', 'status_example'),
                    ('external_id', 'external_id_example'),
                    ('limit', 56),
                    ('batch_token', 'batch_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/employees',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_employee(client):
    """Test case for retrieve_employee

    RetrieveEmployee
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/employees/{employee_id}'.format(employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_employee_role(client):
    """Test case for retrieve_employee_role

    RetrieveEmployeeRole
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/roles/{role_id}'.format(role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_employee(client):
    """Test case for update_employee

    UpdateEmployee
    """
    body = {"updated_at":"updated_at","created_at":"created_at","last_name":"last_name","external_id":"external_id","id":"id","first_name":"first_name","email":"email","role_ids":["role_ids","role_ids"],"authorized_location_ids":["authorized_location_ids","authorized_location_ids"],"status":"status"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/employees/{employee_id}'.format(employee_id='employee_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_employee_role(client):
    """Test case for update_employee_role

    UpdateEmployeeRole
    """
    body = {"updated_at":"updated_at","is_owner":True,"permissions":["permissions","permissions"],"name":"name","created_at":"created_at","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/roles/{role_id}'.format(role_id='role_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

