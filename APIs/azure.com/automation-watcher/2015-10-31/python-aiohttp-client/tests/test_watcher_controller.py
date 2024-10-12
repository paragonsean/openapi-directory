# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.watcher import Watcher
from openapi_server.models.watcher_list_by_automation_account_default_response import WatcherListByAutomationAccountDefaultResponse
from openapi_server.models.watcher_list_result import WatcherListResult
from openapi_server.models.watcher_update_parameters import WatcherUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_watcher_create_or_update(client):
    """Test case for watcher_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"scriptParameters":{"key":"scriptParameters"},"scriptRunOn":"scriptRunOn","lastModifiedTime":"2000-01-23T04:56:07.000+00:00","creationTime":"2000-01-23T04:56:07.000+00:00","lastModifiedBy":"lastModifiedBy","description":"description","scriptName":"scriptName","executionFrequencyInSeconds":0,"status":"status"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/watchers/{watcher_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', watcher_name='watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_watcher_delete(client):
    """Test case for watcher_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/watchers/{watcher_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', watcher_name='watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_watcher_get(client):
    """Test case for watcher_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/watchers/{watcher_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', watcher_name='watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_watcher_list_by_automation_account(client):
    """Test case for watcher_list_by_automation_account

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/watchers'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_watcher_start(client):
    """Test case for watcher_start

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/watchers/{watcher_name}/start'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', watcher_name='watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_watcher_stop(client):
    """Test case for watcher_stop

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/watchers/{watcher_name}/stop'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', watcher_name='watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_watcher_update(client):
    """Test case for watcher_update

    
    """
    parameters = {"name":"name","properties":{"executionFrequencyInSeconds":0}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/watchers/{watcher_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', watcher_name='watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

