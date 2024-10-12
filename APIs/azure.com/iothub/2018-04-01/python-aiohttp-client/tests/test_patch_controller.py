# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.iot_hub_description import IotHubDescription
from openapi_server.models.tags_resource import TagsResource


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_update(client):
    """Test case for iot_hub_resource_update

    Update an existing IoT Hubs tags.
    """
    iot_hub_tags = {"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=iot_hub_tags,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

