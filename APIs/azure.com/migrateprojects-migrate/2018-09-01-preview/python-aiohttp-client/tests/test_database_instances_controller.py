# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.database_instance import DatabaseInstance
from openapi_server.models.database_instance_collection import DatabaseInstanceCollection


pytestmark = pytest.mark.asyncio

async def test_database_instances_enumerate_database_instances(client):
    """Test case for database_instances_enumerate_database_instances

    Gets a list of database instances in the migrate project.
    """
    params = [('api-version', 'api_version_example'),
                    ('continuationToken', 'continuation_token_example'),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/databaseInstances'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_instances_get_database_instance(client):
    """Test case for database_instances_get_database_instance

    Gets a database instance in the migrate project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/databaseInstances/{database_instance_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example', database_instance_name='database_instance_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

