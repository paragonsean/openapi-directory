# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.rerun_trigger_list_response import RerunTriggerListResponse
from openapi_server.models.rerun_tumbling_window_trigger_action_parameters import RerunTumblingWindowTriggerActionParameters
from openapi_server.models.trigger_resource import TriggerResource


pytestmark = pytest.mark.asyncio

async def test_rerun_triggers_cancel(client):
    """Test case for rerun_triggers_cancel

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/triggers/{trigger_name}/rerunTriggers/{rerun_trigger_name}/cancel'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', trigger_name='trigger_name_example', rerun_trigger_name='rerun_trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rerun_triggers_create(client):
    """Test case for rerun_triggers_create

    
    """
    rerun_tumbling_window_trigger_action_parameters = {"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","maxConcurrency":4}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/triggers/{trigger_name}/rerunTriggers/{rerun_trigger_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', trigger_name='trigger_name_example', rerun_trigger_name='rerun_trigger_name_example'),
        headers=headers,
        json=rerun_tumbling_window_trigger_action_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rerun_triggers_list_by_trigger(client):
    """Test case for rerun_triggers_list_by_trigger

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/triggers/{trigger_name}/rerunTriggers'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rerun_triggers_start(client):
    """Test case for rerun_triggers_start

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/triggers/{trigger_name}/rerunTriggers/{rerun_trigger_name}/start'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', trigger_name='trigger_name_example', rerun_trigger_name='rerun_trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rerun_triggers_stop(client):
    """Test case for rerun_triggers_stop

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/triggers/{trigger_name}/rerunTriggers/{rerun_trigger_name}/stop'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', trigger_name='trigger_name_example', rerun_trigger_name='rerun_trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

