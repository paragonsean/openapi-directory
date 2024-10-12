# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_usergroups_add_channels(client):
    """Test case for admin_usergroups_add_channels

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_ids': 'channel_ids_example',
        'team_id': 'team_id_example',
        'usergroup_id': 'usergroup_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.usergroups.addChannels',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_usergroups_add_teams(client):
    """Test case for admin_usergroups_add_teams

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'auto_provision': True,
        'team_ids': 'team_ids_example',
        'usergroup_id': 'usergroup_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.usergroups.addTeams',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_usergroups_list_channels(client):
    """Test case for admin_usergroups_list_channels

    
    """
    params = [('usergroup_id', 'usergroup_id_example'),
                    ('team_id', 'team_id_example'),
                    ('include_num_members', True)]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.usergroups.listChannels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_usergroups_remove_channels(client):
    """Test case for admin_usergroups_remove_channels

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_ids': 'channel_ids_example',
        'usergroup_id': 'usergroup_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.usergroups.removeChannels',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

