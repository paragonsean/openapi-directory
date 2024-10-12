# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.trigger import Trigger
from openapi_server.models.trigger_list import TriggerList


pytestmark = pytest.mark.asyncio

async def test_triggers_create_or_update(client):
    """Test case for triggers_create_or_update

    
    """
    trigger = {"kind":"FileEvent"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/triggers/{name}'.format(device_name='device_name_example', name='name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/triggers/{name}'.format(device_name='device_name_example', name='name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_triggers_get(client):
    """Test case for triggers_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/triggers/{name}'.format(device_name='device_name_example', name='name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_triggers_list_by_data_box_edge_device(client):
    """Test case for triggers_list_by_data_box_edge_device

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{device_name}/triggers'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

