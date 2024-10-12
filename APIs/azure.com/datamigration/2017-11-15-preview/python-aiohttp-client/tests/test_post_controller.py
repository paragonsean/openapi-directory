# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server.models.services_check_name_availability200_response import ServicesCheckNameAvailability200Response
from openapi_server.models.services_check_name_availability_request import ServicesCheckNameAvailabilityRequest
from openapi_server.models.services_check_status200_response import ServicesCheckStatus200Response
from openapi_server.models.tasks_get200_response import TasksGet200Response


pytestmark = pytest.mark.asyncio

async def test_services_check_children_name_availability_0(client):
    """Test case for services_check_children_name_availability_0

    Check nested resource name validity and availability
    """
    parameters = openapi_server.ServicesCheckNameAvailabilityRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}/checkNameAvailability'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_check_name_availability_0(client):
    """Test case for services_check_name_availability_0

    Check name validity and availability
    """
    parameters = openapi_server.ServicesCheckNameAvailabilityRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataMigration/locations/{location}/checkNameAvailability'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_check_status_1(client):
    """Test case for services_check_status_1

    Check service health status
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}/checkStatus'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_start_1(client):
    """Test case for services_start_1

    Start service
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}/start'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_stop_1(client):
    """Test case for services_stop_1

    Stop service
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}/stop'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_cancel_1(client):
    """Test case for tasks_cancel_1

    Cancel a task
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}/projects/{project_name}/tasks/{task_name}/cancel'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example', project_name='project_name_example', task_name='task_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

