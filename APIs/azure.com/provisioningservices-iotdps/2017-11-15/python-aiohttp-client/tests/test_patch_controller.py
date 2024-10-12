# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.provisioning_service_description import ProvisioningServiceDescription
from openapi_server.models.tags_resource import TagsResource


pytestmark = pytest.mark.asyncio

async def test_iot_dps_resource_update(client):
    """Test case for iot_dps_resource_update

    Update an existing provisioning service's tags.
    """
    provisioning_service_tags = {"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices/{provisioning_service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', provisioning_service_name='provisioning_service_name_example'),
        headers=headers,
        json=provisioning_service_tags,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

