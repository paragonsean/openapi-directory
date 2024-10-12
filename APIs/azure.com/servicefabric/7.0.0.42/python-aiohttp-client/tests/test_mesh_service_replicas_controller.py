# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_service_replica_description_list import PagedServiceReplicaDescriptionList
from openapi_server.models.service_replica_description import ServiceReplicaDescription


pytestmark = pytest.mark.asyncio

async def test_mesh_service_replica_get(client):
    """Test case for mesh_service_replica_get

    Gets the given replica of the service of an application.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Applications/{application_resource_name}/Services/{service_resource_name}/Replicas/{replica_name}'.format(application_resource_name='application_resource_name_example', service_resource_name='service_resource_name_example', replica_name='replica_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_service_replica_list(client):
    """Test case for mesh_service_replica_list

    Lists all the replicas of a service.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Applications/{application_resource_name}/Services/{service_resource_name}/Replicas'.format(application_resource_name='application_resource_name_example', service_resource_name='service_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

