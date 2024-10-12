# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.trigger_list_response import TriggerListResponse
from openapi_server.models.trigger_resource import TriggerResource
from openapi_server.models.trigger_run_list_response import TriggerRunListResponse


pytestmark = pytest.mark.asyncio

async def test_triggers_create_or_update(client):
    """Test case for triggers_create_or_update

    
    """
    trigger = {"properties":{"key":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/triggers/{trigger_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        json=trigger,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_triggers_delete(client):
    """Test case for triggers_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/triggers/{trigger_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_triggers_list_by_factory(client):
    """Test case for triggers_list_by_factory

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/triggers'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_triggers_list_runs(client):
    """Test case for triggers_list_runs

    
    """
    params = [('api-version', 'api_version_example'),
                    ('startTime', '2013-10-20T19:20:30+01:00'),
                    ('endTime', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/triggers/{trigger_name}/triggerruns'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_triggers_start(client):
    """Test case for triggers_start

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/triggers/{trigger_name}/start'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_triggers_stop(client):
    """Test case for triggers_stop

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/triggers/{trigger_name}/stop'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

