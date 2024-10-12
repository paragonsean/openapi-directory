# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.iot_hub_description import IotHubDescription


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_delete(client):
    """Test case for iot_hub_resource_delete

    Delete an IoT hub.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_delete_event_hub_consumer_group(client):
    """Test case for iot_hub_resource_delete_event_hub_consumer_group

    Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/eventHubEndpoints/{event_hub_endpoint_name}/ConsumerGroups/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', event_hub_endpoint_name='event_hub_endpoint_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

