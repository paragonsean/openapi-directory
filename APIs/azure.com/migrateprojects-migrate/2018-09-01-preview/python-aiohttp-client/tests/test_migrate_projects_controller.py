# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.migrate_project import MigrateProject
from openapi_server.models.refresh_summary_input import RefreshSummaryInput
from openapi_server.models.refresh_summary_result import RefreshSummaryResult
from openapi_server.models.register_tool_input import RegisterToolInput
from openapi_server.models.registration_result import RegistrationResult


pytestmark = pytest.mark.asyncio

async def test_migrate_projects_delete_migrate_project(client):
    """Test case for migrate_projects_delete_migrate_project

    Delete the migrate project
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrate_projects_get_migrate_project(client):
    """Test case for migrate_projects_get_migrate_project

    Method to get a migrate project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrate_projects_patch_migrate_project(client):
    """Test case for migrate_projects_patch_migrate_project

    Update migrate project.
    """
    body = {"name":"name","eTag":"eTag","location":"location","id":"id","type":"type","properties":{"summary":{"key":{"instanceType":"instanceType","lastSummaryRefreshedTime":"2000-01-23T04:56:07.000+00:00","refreshSummaryState":"Started","extendedSummary":{"key":"extendedSummary"}}},"lastSummaryRefreshedTime":"2000-01-23T04:56:07.000+00:00","registeredTools":["ServerDiscovery","ServerDiscovery"],"refreshSummaryState":"Started","provisioningState":"Accepted"},"tags":{"additionalProperties":"additionalProperties"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrate_projects_put_migrate_project(client):
    """Test case for migrate_projects_put_migrate_project

    Method to create or update a migrate project.
    """
    body = {"name":"name","eTag":"eTag","location":"location","id":"id","type":"type","properties":{"summary":{"key":{"instanceType":"instanceType","lastSummaryRefreshedTime":"2000-01-23T04:56:07.000+00:00","refreshSummaryState":"Started","extendedSummary":{"key":"extendedSummary"}}},"lastSummaryRefreshedTime":"2000-01-23T04:56:07.000+00:00","registeredTools":["ServerDiscovery","ServerDiscovery"],"refreshSummaryState":"Started","provisioningState":"Accepted"},"tags":{"additionalProperties":"additionalProperties"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrate_projects_refresh_migrate_project_summary(client):
    """Test case for migrate_projects_refresh_migrate_project_summary

    Refresh the summary of the migrate project.
    """
    input = {"goal":"Servers"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/refreshSummary'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrate_projects_register_tool(client):
    """Test case for migrate_projects_register_tool

    Registers a tool with the migrate project.
    """
    input = {"tool":"ServerDiscovery"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/registerTool'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

