# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_my_sql_database import CreateMySqlDatabase
from openapi_server.models.create_my_sql_user import CreateMySqlUser
from openapi_server.models.my_sql_database import MySqlDatabase
from openapi_server.models.my_sql_user import MySqlUser
from openapi_server.models.update_user_password_request import UpdateUserPasswordRequest
from openapi_server.models.update_user_status_request import UpdateUserStatusRequest


pytestmark = pytest.mark.asyncio

async def test_change_database_user_password(client):
    """Test case for change_database_user_password

    Change password for mysql user
    """
    body = {"password":"password"}
    params = [('database_name', 'database_name_example'),
                    ('user_name', 'user_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/mysqldatabases/{database_name}/users/{user_name}/password'.format(database_name2='database_name_example', user_name2='user_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_database_user_status(client):
    """Test case for change_database_user_status

    Enable/disable mysql user
    """
    body = {"enabled":True}
    params = [('database_name', 'database_name_example'),
                    ('user_name', 'user_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/mysqldatabases/{database_name}/users/{user_name}/status'.format(database_name2='database_name_example', user_name2='user_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_my_sql_database(client):
    """Test case for create_my_sql_database

    Create a new mysql database
    """
    body = {"password":"password","account_id":0,"database_name":"database_name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/mysqldatabases',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_my_sql_user(client):
    """Test case for create_my_sql_user

    Create a new mysql user
    """
    body = {"password":"password","name":"name"}
    params = [('database_name', 'database_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/mysqldatabases/{database_name}/users'.format(database_name2='database_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_database(client):
    """Test case for delete_database

    Delete a mysql database
    """
    params = [('database_name', 'database_name_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/mysqldatabases/{database_name}'.format(database_name2='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_database_user(client):
    """Test case for delete_database_user

    Delete a mysql user
    """
    params = [('database_name', 'database_name_example'),
                    ('user_name', 'user_name_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/mysqldatabases/{database_name}/users/{user_name}'.format(database_name2='database_name_example', user_name2='user_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_database_users(client):
    """Test case for get_database_users

    Overview of mysql users
    """
    params = [('database_name', 'database_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/mysqldatabases/{database_name}/users'.format(database_name2='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_my_sql_database(client):
    """Test case for get_my_sql_database

    Get a specific database
    """
    params = [('database_name', 'database_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/mysqldatabases/{database_name}'.format(database_name2='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_my_sql_databases(client):
    """Test case for get_my_sql_databases

    Overview of mysql databases
    """
    params = [('skip', 56),
                    ('take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/mysqldatabases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

