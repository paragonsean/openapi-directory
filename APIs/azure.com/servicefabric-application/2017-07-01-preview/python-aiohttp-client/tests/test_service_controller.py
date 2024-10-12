# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.service_resource import ServiceResource
from openapi_server.models.service_resource_list import ServiceResourceList
from openapi_server.models.service_resource_update import ServiceResourceUpdate


pytestmark = pytest.mark.asyncio

async def test_services_create(client):
    """Test case for services_create

    Creates or updates a Service Fabric service resource.
    """
    parameters = {"properties":{"serviceKind":"Invalid","partitionDescription":{"PartitionScheme":"Invalid"},"provisioningState":"provisioningState","serviceTypeName":"serviceTypeName"}}
    params = [('api-version', 2017-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}/applications/{application_name}/services/{service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_name='application_name_example', service_name='service_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_delete(client):
    """Test case for services_delete

    Deletes a Service Fabric service resource.
    """
    params = [('api-version', 2017-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}/applications/{application_name}/services/{service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_name='application_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_get(client):
    """Test case for services_get

    Gets a Service Fabric service resource.
    """
    params = [('api-version', 2017-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}/applications/{application_name}/services/{service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_name='application_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list(client):
    """Test case for services_list

    Gets the list of service resources created in the specified Service Fabric application resource.
    """
    params = [('api-version', 2017-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}/applications/{application_name}/services'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_update(client):
    """Test case for services_update

    Updates a Service Fabric service resource.
    """
    parameters = {"properties":{"serviceKind":"Invalid"}}
    params = [('api-version', 2017-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}/applications/{application_name}/services/{service_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_name='application_name_example', service_name='service_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

