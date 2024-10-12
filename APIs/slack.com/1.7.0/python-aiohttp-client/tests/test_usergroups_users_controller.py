# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.usergroups_users_list_error_schema import UsergroupsUsersListErrorSchema
from openapi_server.models.usergroups_users_list_schema import UsergroupsUsersListSchema
from openapi_server.models.usergroups_users_update_error_schema import UsergroupsUsersUpdateErrorSchema
from openapi_server.models.usergroups_users_update_schema import UsergroupsUsersUpdateSchema


pytestmark = pytest.mark.asyncio

async def test_usergroups_users_list(client):
    """Test case for usergroups_users_list

    
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
async def test_usergroups_users_update(client):
    """Test case for usergroups_users_update

    
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

