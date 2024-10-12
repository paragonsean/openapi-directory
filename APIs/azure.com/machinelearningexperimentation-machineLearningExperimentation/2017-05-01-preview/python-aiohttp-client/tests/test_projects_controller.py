# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.project import Project
from openapi_server.models.project_list_result import ProjectListResult
from openapi_server.models.project_update_parameters import ProjectUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_projects_create_or_update(client):
    """Test case for projects_create_or_update

    
    """
    parameters = {"properties":{"accountId":"accountId","gitrepo":"gitrepo","description":"description","provisioningState":"Creating","creationDate":"2000-01-23T04:56:07.000+00:00","projectId":"projectId","friendlyName":"friendlyName","workspaceId":"workspaceId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningExperimentation/accounts/{account_name}/workspaces/{workspace_name}/projects/{project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', workspace_name='workspace_name_example', project_name='project_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_delete(client):
    """Test case for projects_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningExperimentation/accounts/{account_name}/workspaces/{workspace_name}/projects/{project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', workspace_name='workspace_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get(client):
    """Test case for projects_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningExperimentation/accounts/{account_name}/workspaces/{workspace_name}/projects/{project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', workspace_name='workspace_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_list_by_workspace(client):
    """Test case for projects_list_by_workspace

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningExperimentation/accounts/{account_name}/workspaces{workspaceName}/projects'.format(subscription_id='subscription_id_example', account_name='account_name_example', workspace_name='workspace_name_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_update(client):
    """Test case for projects_update

    
    """
    parameters = {"properties":{"gitrepo":"gitrepo","description":"description","friendlyName":"friendlyName"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningExperimentation/accounts/{account_name}/workspaces/{workspace_name}/projects/{project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', workspace_name='workspace_name_example', project_name='project_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

