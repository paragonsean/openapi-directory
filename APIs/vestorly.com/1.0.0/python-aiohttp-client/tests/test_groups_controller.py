# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.group_input import GroupInput
from openapi_server.models.groupresponse import Groupresponse
from openapi_server.models.groups import Groups


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_group(client):
    """Test case for create_group

    
    """
    group = openapi_server.GroupInput()
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/groups',
        headers=headers,
        json=group,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_group(client):
    """Test case for delete_group

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/groups/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_group_by_id(client):
    """Test case for find_group_by_id

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/groups/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_groups(client):
    """Test case for find_groups

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_group_by_id(client):
    """Test case for update_group_by_id

    
    """
    group = openapi_server.GroupInput()
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/groups/{id}'.format(id='id_example'),
        headers=headers,
        json=group,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

