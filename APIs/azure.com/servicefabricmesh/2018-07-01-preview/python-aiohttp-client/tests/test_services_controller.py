# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_list import ServiceList
from openapi_server.models.service_resource_description import ServiceResourceDescription


pytestmark = pytest.mark.asyncio

async def test_service_get(client):
    """Test case for service_get

    Gets the properties of the service.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/applications/{application_name}/services/{service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_list_by_application_name(client):
    """Test case for service_list_by_application_name

    Gets services of a given application.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/applications/{application_name}/services'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

