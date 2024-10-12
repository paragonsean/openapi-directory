# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.solution import Solution
from openapi_server.models.solution_config import SolutionConfig
from openapi_server.models.solutions_collection import SolutionsCollection


pytestmark = pytest.mark.asyncio

async def test_solutions_cleanup_solution_data(client):
    """Test case for solutions_cleanup_solution_data

    Cleanup the solution data in the migrate project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/solutions/{solution_name}/cleanupData'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example', solution_name='solution_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_solutions_delete_solution(client):
    """Test case for solutions_delete_solution

    Delete the solution
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/solutions/{solution_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example', solution_name='solution_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_solutions_enumerate_solutions(client):
    """Test case for solutions_enumerate_solutions

    Gets the list of solutions in the migrate project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/solutions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_solutions_get_config(client):
    """Test case for solutions_get_config

    Gets the config for the solution in the migrate project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/solutions/{solution_name}/getConfig'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example', solution_name='solution_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_solutions_get_solution(client):
    """Test case for solutions_get_solution

    Gets a solution in the migrate project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/solutions/{solution_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example', solution_name='solution_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_solutions_patch_solution(client):
    """Test case for solutions_patch_solution

    Update solution.
    """
    solution_input = {"name":"name","etag":"etag","id":"id","type":"type","properties":{"summary":{"instanceType":"instanceType"},"goal":"Servers","purpose":"Discovery","cleanupState":"None","details":{"extendedDetails":{"key":"extendedDetails"},"assessmentCount":0,"groupCount":6},"tool":"ServerDiscovery","status":"Inactive"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/solutions/{solution_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example', solution_name='solution_name_example'),
        headers=headers,
        json=solution_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_solutions_put_solution(client):
    """Test case for solutions_put_solution

    Creates a solution in the migrate project.
    """
    solution_input = {"name":"name","etag":"etag","id":"id","type":"type","properties":{"summary":{"instanceType":"instanceType"},"goal":"Servers","purpose":"Discovery","cleanupState":"None","details":{"extendedDetails":{"key":"extendedDetails"},"assessmentCount":0,"groupCount":6},"tool":"ServerDiscovery","status":"Inactive"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/solutions/{solution_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example', solution_name='solution_name_example'),
        headers=headers,
        json=solution_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

