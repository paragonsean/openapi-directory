# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection_setting import ConnectionSetting
from openapi_server.models.connection_setting_response_list import ConnectionSettingResponseList
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_bot_connection_create(client):
    """Test case for bot_connection_create

    
    """
    parameters = {"properties":{"clientId":"clientId","serviceProviderId":"serviceProviderId","serviceProviderDisplayName":"serviceProviderDisplayName","clientSecret":"clientSecret","scopes":"scopes","parameters":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"settingId":"settingId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}/Connections/{connection_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', connection_name='connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bot_connection_delete(client):
    """Test case for bot_connection_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}/Connections/{connection_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', connection_name='connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bot_connection_get(client):
    """Test case for bot_connection_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}/Connections/{connection_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', connection_name='connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bot_connection_list_by_bot_service(client):
    """Test case for bot_connection_list_by_bot_service

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}/connections'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bot_connection_list_with_secrets(client):
    """Test case for bot_connection_list_with_secrets

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}/Connections/{connection_name}/listWithSecrets'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', connection_name='connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bot_connection_update(client):
    """Test case for bot_connection_update

    
    """
    parameters = {"properties":{"clientId":"clientId","serviceProviderId":"serviceProviderId","serviceProviderDisplayName":"serviceProviderDisplayName","clientSecret":"clientSecret","scopes":"scopes","parameters":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"settingId":"settingId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.BotService/botServices/{resource_name}/Connections/{connection_name}'.format(resource_group_name='resource_group_name_example', resource_name='resource_name_example', connection_name='connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

