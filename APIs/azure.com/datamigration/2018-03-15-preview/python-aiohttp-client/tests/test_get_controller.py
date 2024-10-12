# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operations_list200_response import OperationsList200Response
from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server.models.projects_get200_response import ProjectsGet200Response
from openapi_server.models.projects_list200_response import ProjectsList200Response
from openapi_server.models.resource_skus_list_skus200_response import ResourceSkusListSkus200Response
from openapi_server.models.services_get200_response import ServicesGet200Response
from openapi_server.models.services_list200_response import ServicesList200Response
from openapi_server.models.services_list_skus200_response import ServicesListSkus200Response
from openapi_server.models.tasks_get200_response import TasksGet200Response
from openapi_server.models.tasks_list200_response import TasksList200Response
from openapi_server.models.usages_list200_response import UsagesList200Response


pytestmark = pytest.mark.asyncio

async def test_operations_list_0(client):
    """Test case for operations_list_0

    Get available resource provider actions (operations)
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.DataMigration/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get_1(client):
    """Test case for projects_get_1

    Get project information
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}/projects/{project_name}'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_list_1(client):
    """Test case for projects_list_1

    Get projects in a service
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}/projects'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resource_skus_list_skus_0(client):
    """Test case for resource_skus_list_skus_0

    Get supported SKUs
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataMigration/skus'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_get_1(client):
    """Test case for services_get_1

    Get DMS Service Instance
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_1(client):
    """Test case for services_list_1

    Get services in subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataMigration/services'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_by_resource_group_1(client):
    """Test case for services_list_by_resource_group_1

    Get services in resource group
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services'.format(subscription_id='subscription_id_example', group_name='group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_skus_1(client):
    """Test case for services_list_skus_1

    Get compatible SKUs
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}/skus'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_get_1(client):
    """Test case for tasks_get_1

    Get task information
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}/projects/{project_name}/tasks/{task_name}'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example', project_name='project_name_example', task_name='task_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_list_1(client):
    """Test case for tasks_list_1

    Get tasks in a service
    """
    params = [('api-version', 'api_version_example'),
                    ('taskType', 'task_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}/projects/{project_name}/tasks'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_usages_list_0(client):
    """Test case for usages_list_0

    Get resource quotas and usage information
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataMigration/locations/{location}/usages'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

