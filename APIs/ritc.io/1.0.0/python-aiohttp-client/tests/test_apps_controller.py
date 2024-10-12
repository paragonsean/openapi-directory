# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app import App
from openapi_server.models.app_channel_response import AppChannelResponse
from openapi_server.models.app_external_credentials import AppExternalCredentials
from openapi_server.models.app_external_credentials_response import AppExternalCredentialsResponse
from openapi_server.models.app_response import AppResponse
from openapi_server.models.rule_results import RuleResults


pytestmark = pytest.mark.asyncio

async def test_add_app(client):
    """Test case for add_app

    
    """
    app_object = {"name":"name","desc":"desc"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps',
        headers=headers,
        json=app_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_app_channel_user(client):
    """Test case for add_app_channel_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/channels/{channel_id}/users/{user_id}'.format(channel_id='channel_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_channel_external_credentials(client):
    """Test case for add_channel_external_credentials

    
    """
    app_external_credentials_object = {"credentials":"{}","name":"name","authType":"apikey","channel_id":"channel_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/ext/api/credentials',
        headers=headers,
        json=app_external_credentials_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_app(client):
    """Test case for get_app

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_app_channel_user(client):
    """Test case for get_app_channel_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/channels/{channel_id}/users/{user_id}'.format(channel_id='channel_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_external_credentials(client):
    """Test case for get_channel_external_credentials

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/ext/api/credentials/{channel_id}'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_app_channel_users(client):
    """Test case for list_app_channel_users

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/channels/{channel_id}/users'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_app_channels(client):
    """Test case for list_app_channels

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/channels/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_apps(client):
    """Test case for list_apps

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channel_external_credentials(client):
    """Test case for list_channel_external_credentials

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apps/ext/api/credentials',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_app(client):
    """Test case for remove_app

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_channel_external_credentials(client):
    """Test case for remove_channel_external_credentials

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apps/ext/api/credentials/{channel_id}'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_app(client):
    """Test case for run_app

    
    """
    initial_data = None
    params = [('break_when_rule_fires', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/rules/run',
        headers=headers,
        json=initial_data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_rule_group(client):
    """Test case for run_rule_group

    
    """
    initial_data = None
    params = [('break_when_rule_fires', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apps/rulegroup/run/{rule_id_list}'.format(rule_id_list='rule_id_list_example'),
        headers=headers,
        json=initial_data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_app(client):
    """Test case for update_app

    
    """
    app_object = {"name":"name","desc":"desc"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/apps/{app_id}'.format(app_id='app_id_example'),
        headers=headers,
        json=app_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_channel_external_credentials(client):
    """Test case for update_channel_external_credentials

    
    """
    app_external_credentials_object = {"credentials":"{}","name":"name","authType":"apikey","channel_id":"channel_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/apps/ext/api/credentials/{channel_id}'.format(channel_id='channel_id_example'),
        headers=headers,
        json=app_external_credentials_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

