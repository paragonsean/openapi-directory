# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_service_resource_description_list import PagedServiceResourceDescriptionList
from openapi_server.models.service_resource_description import ServiceResourceDescription


pytestmark = pytest.mark.asyncio

async def test_mesh_service_get(client):
    """Test case for mesh_service_get

    Gets the Service resource with the given name.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Applications/{application_resource_name}/Services/{service_resource_name}'.format(application_resource_name='application_resource_name_example', service_resource_name='service_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_service_list(client):
    """Test case for mesh_service_list

    Lists all the service resources.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Applications/{application_resource_name}/Services'.format(application_resource_name='application_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

