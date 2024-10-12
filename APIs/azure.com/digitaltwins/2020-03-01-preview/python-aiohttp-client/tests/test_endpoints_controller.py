# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.digital_twins_endpoint_resource import DigitalTwinsEndpointResource
from openapi_server.models.digital_twins_endpoint_resource_list_result import DigitalTwinsEndpointResourceListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_digital_twins_endpoint_create_or_update(client):
    """Test case for digital_twins_endpoint_create_or_update

    
    """
    endpoint_description = {"properties":{"endpointType":"EventHub","createdTime":"2000-01-23T04:56:07.000+00:00","provisioningState":"Provisioning","tags":{"key":"tags"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resource_name}/endpoints/{endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', endpoint_name='endpoint_name_example'),
        headers=headers,
        json=endpoint_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_digital_twins_endpoint_delete(client):
    """Test case for digital_twins_endpoint_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resource_name}/endpoints/{endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', endpoint_name='endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_digital_twins_endpoint_get(client):
    """Test case for digital_twins_endpoint_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resource_name}/endpoints/{endpoint_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', endpoint_name='endpoint_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_digital_twins_endpoint_list(client):
    """Test case for digital_twins_endpoint_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resource_name}/endpoints'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

