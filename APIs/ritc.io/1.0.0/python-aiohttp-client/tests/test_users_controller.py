# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.admin_user import AdminUser
from openapi_server.models.admin_user_response import AdminUserResponse
from openapi_server.models.app_user import AppUser
from openapi_server.models.app_user_response import AppUserResponse
from openapi_server.models.authorize_url_response import AuthorizeUrlResponse
from openapi_server.models.rule_full_response import RuleFullResponse
from openapi_server.models.rule_short_response import RuleShortResponse
from openapi_server.models.user_channel import UserChannel


pytestmark = pytest.mark.asyncio

async def test_add_admin_user(client):
    """Test case for add_admin_user

    
    """
    admin_user_object = {"password":"password","type":"admin","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/admin',
        headers=headers,
        json=admin_user_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_app_user(client):
    """Test case for add_app_user

    
    """
    app_user_object = {"password":"password","name":"name","config":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users',
        headers=headers,
        json=app_user_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_app_user_to_channel(client):
    """Test case for add_app_user_to_channel

    
    """
    channel_id = 'channel_id_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{user_id}/channels'.format(user_id='user_id_example'),
        headers=headers,
        json=channel_id,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_app_user_to_rule(client):
    """Test case for add_app_user_to_rule

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{user_id}/rules/{rule_id}'.format(user_id='user_id_example', rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authenticate_app_user_for_channel(client):
    """Test case for authenticate_app_user_for_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/authenticate/{user_id}/channel/{channel_id}'.format(user_id='user_id_example', channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_admin_user(client):
    """Test case for get_admin_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/admin/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_app_user(client):
    """Test case for get_app_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_app_user_channel(client):
    """Test case for get_app_user_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/channels/{channel_id}'.format(user_id='user_id_example', channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_app_user_rule(client):
    """Test case for get_app_user_rule

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/rules/{rule_id}'.format(user_id='user_id_example', rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_admin_users(client):
    """Test case for list_admin_users

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/admin',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_app_user_channels(client):
    """Test case for list_app_user_channels

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/channels'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_app_user_rules(client):
    """Test case for list_app_user_rules

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/rules'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_app_users(client):
    """Test case for list_app_users

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_admin_user(client):
    """Test case for remove_admin_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/admin/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_app_user(client):
    """Test case for remove_app_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_app_user_from_channel(client):
    """Test case for remove_app_user_from_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_id}/channels/{channel_id}'.format(user_id='user_id_example', channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_app_user_from_rule(client):
    """Test case for remove_app_user_from_rule

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_id}/rules/{rule_id}'.format(user_id='user_id_example', rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_rule_for_app_user(client):
    """Test case for run_rule_for_app_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{user_id}/rules/{rule_id}/run'.format(user_id='user_id_example', rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_admin_user(client):
    """Test case for update_admin_user

    
    """
    admin_user_object = {"password":"password","type":"admin","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/users/admin/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        json=admin_user_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_app_user(client):
    """Test case for update_app_user

    
    """
    app_user_object = {"password":"password","name":"name","config":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        json=app_user_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

