# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.service_resource_description import ServiceResourceDescription
from openapi_server.models.service_resource_description_list import ServiceResourceDescriptionList


pytestmark = pytest.mark.asyncio

async def test_service_get(client):
    """Test case for service_get

    Gets the service resource with the given name.
    """
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/applications/{application_resource_name}/services/{service_resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_resource_name='application_resource_name_example', service_resource_name='service_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_list(client):
    """Test case for service_list

    Lists all the service resources.
    """
    params = [('api-version', 2018-09-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/applications/{application_resource_name}/services'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_resource_name='application_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

