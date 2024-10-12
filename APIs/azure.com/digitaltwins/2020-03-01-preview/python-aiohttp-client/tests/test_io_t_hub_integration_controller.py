# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.digital_twins_integration_resource_list_result import DigitalTwinsIntegrationResourceListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.integration_resource import IntegrationResource


pytestmark = pytest.mark.asyncio

async def test_digital_twins_io_t_hubs_list(client):
    """Test case for digital_twins_io_t_hubs_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resource_name}/integrationResources'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_io_t_hub_create_or_update(client):
    """Test case for io_t_hub_create_or_update

    
    """
    iot_hub_description = {"properties":{"resourceId":"resourceId","createdTime":"2000-01-23T04:56:07.000+00:00"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{scope}/providers/Microsoft.DigitalTwins/integrationResources/{integration_resource_name}'.format(scope='scope_example', integration_resource_name='integration_resource_name_example'),
        headers=headers,
        json=iot_hub_description,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_io_t_hub_delete(client):
    """Test case for io_t_hub_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{scope}/providers/Microsoft.DigitalTwins/integrationResources/{integration_resource_name}'.format(scope='scope_example', integration_resource_name='integration_resource_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_io_t_hub_get(client):
    """Test case for io_t_hub_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.DigitalTwins/integrationResources/{integration_resource_name}'.format(scope='scope_example', integration_resource_name='integration_resource_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

