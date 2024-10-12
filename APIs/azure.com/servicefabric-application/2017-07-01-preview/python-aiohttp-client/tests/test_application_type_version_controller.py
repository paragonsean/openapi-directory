# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_type_version_resource import ApplicationTypeVersionResource
from openapi_server.models.application_type_version_resource_list import ApplicationTypeVersionResourceList
from openapi_server.models.error_model import ErrorModel


pytestmark = pytest.mark.asyncio

async def test_application_type_versions_create(client):
    """Test case for application_type_versions_create

    Creates or updates a Service Fabric application type version resource.
    """
    parameters = {"properties":{"defaultParameterList":{"key":"defaultParameterList"},"appPackageUrl":"appPackageUrl","provisioningState":"provisioningState"}}
    params = [('api-version', 2017-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}/applicationTypes/{application_type_name}/versions/{version}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_type_name='application_type_name_example', version='version_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_type_versions_delete(client):
    """Test case for application_type_versions_delete

    Deletes a Service Fabric application type version resource.
    """
    params = [('api-version', 2017-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}/applicationTypes/{application_type_name}/versions/{version}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_type_name='application_type_name_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_type_versions_get(client):
    """Test case for application_type_versions_get

    Gets a Service Fabric application type version resource.
    """
    params = [('api-version', 2017-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}/applicationTypes/{application_type_name}/versions/{version}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_type_name='application_type_name_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_type_versions_list(client):
    """Test case for application_type_versions_list

    Gets the list of application type version resources created in the specified Service Fabric application type name resource.
    """
    params = [('api-version', 2017-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabric/clusters/{cluster_name}/applicationTypes/{application_type_name}/versions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_type_name='application_type_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

