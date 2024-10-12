# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.usergroups_create_error_schema import UsergroupsCreateErrorSchema
from openapi_server.models.usergroups_create_schema import UsergroupsCreateSchema
from openapi_server.models.usergroups_disable_error_schema import UsergroupsDisableErrorSchema
from openapi_server.models.usergroups_disable_schema import UsergroupsDisableSchema
from openapi_server.models.usergroups_enable_error_schema import UsergroupsEnableErrorSchema
from openapi_server.models.usergroups_enable_schema import UsergroupsEnableSchema
from openapi_server.models.usergroups_list_error_schema import UsergroupsListErrorSchema
from openapi_server.models.usergroups_list_schema import UsergroupsListSchema
from openapi_server.models.usergroups_update_error_schema import UsergroupsUpdateErrorSchema
from openapi_server.models.usergroups_update_schema import UsergroupsUpdateSchema
from openapi_server.models.usergroups_users_list_error_schema import UsergroupsUsersListErrorSchema
from openapi_server.models.usergroups_users_list_schema import UsergroupsUsersListSchema
from openapi_server.models.usergroups_users_update_error_schema import UsergroupsUsersUpdateErrorSchema
from openapi_server.models.usergroups_users_update_schema import UsergroupsUsersUpdateSchema


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_usergroups_create(client):
    """Test case for usergroups_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channels': 'channels_example',
        'description': 'description_example',
        'handle': 'handle_example',
        'include_count': True,
        'name': 'name_example'
        }
    response = await client.request(
        method='POST',
        path='/api/usergroups.create',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_usergroups_disable(client):
    """Test case for usergroups_disable

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'include_count': True,
        'usergroup': 'usergroup_example'
        }
    response = await client.request(
        method='POST',
        path='/api/usergroups.disable',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_usergroups_enable(client):
    """Test case for usergroups_enable

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'include_count': True,
        'usergroup': 'usergroup_example'
        }
    response = await client.request(
        method='POST',
        path='/api/usergroups.enable',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_usergroups_list(client):
    """Test case for usergroups_list

    
    """
    params = [('include_users', True),
                    ('token', 'token_example'),
                    ('include_count', True),
                    ('include_disabled', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/usergroups.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_usergroups_update(client):
    """Test case for usergroups_update

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channels': 'channels_example',
        'description': 'description_example',
        'handle': 'handle_example',
        'include_count': True,
        'name': 'name_example',
        'usergroup': 'usergroup_example'
        }
    response = await client.request(
        method='POST',
        path='/api/usergroups.update',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_usergroups_users_list_0(client):
    """Test case for usergroups_users_list_0

    
    """
    params = [('token', 'token_example'),
                    ('include_disabled', True),
                    ('usergroup', 'usergroup_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/usergroups.users.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_usergroups_users_update_0(client):
    """Test case for usergroups_users_update_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'include_count': True,
        'usergroup': 'usergroup_example',
        'users': 'users_example'
        }
    response = await client.request(
        method='POST',
        path='/api/usergroups.users.update',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

