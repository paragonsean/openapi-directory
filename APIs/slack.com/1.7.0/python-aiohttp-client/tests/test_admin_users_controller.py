# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_assign(client):
    """Test case for admin_users_assign

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_ids': 'channel_ids_example',
        'is_restricted': True,
        'is_ultra_restricted': True,
        'team_id': 'team_id_example',
        'user_id': 'user_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.assign',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_invite(client):
    """Test case for admin_users_invite

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_ids': 'channel_ids_example',
        'custom_message': 'custom_message_example',
        'email': 'email_example',
        'guest_expiration_ts': 'guest_expiration_ts_example',
        'is_restricted': True,
        'is_ultra_restricted': True,
        'real_name': 'real_name_example',
        'resend': True,
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.invite',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_users_list(client):
    """Test case for admin_users_list

    
    """
    params = [('team_id', 'team_id_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.users.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_remove(client):
    """Test case for admin_users_remove

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'team_id': 'team_id_example',
        'user_id': 'user_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.remove',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_set_admin(client):
    """Test case for admin_users_set_admin

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'team_id': 'team_id_example',
        'user_id': 'user_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.setAdmin',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_set_expiration(client):
    """Test case for admin_users_set_expiration

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'expiration_ts': 56,
        'team_id': 'team_id_example',
        'user_id': 'user_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.setExpiration',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_set_owner(client):
    """Test case for admin_users_set_owner

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'team_id': 'team_id_example',
        'user_id': 'user_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.setOwner',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_set_regular(client):
    """Test case for admin_users_set_regular

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'team_id': 'team_id_example',
        'user_id': 'user_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.setRegular',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

