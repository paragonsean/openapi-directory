# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_restrict_access_add_group(client):
    """Test case for admin_conversations_restrict_access_add_group

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example',
        'group_id': 'group_id_example',
        'team_id': 'team_id_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.restrictAccess.addGroup',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_conversations_restrict_access_list_groups(client):
    """Test case for admin_conversations_restrict_access_list_groups

    
    """
    params = [('token', 'token_example'),
                    ('channel_id', 'channel_id_example'),
                    ('team_id', 'team_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.conversations.restrictAccess.listGroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_restrict_access_remove_group(client):
    """Test case for admin_conversations_restrict_access_remove_group

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example',
        'group_id': 'group_id_example',
        'team_id': 'team_id_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.restrictAccess.removeGroup',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

