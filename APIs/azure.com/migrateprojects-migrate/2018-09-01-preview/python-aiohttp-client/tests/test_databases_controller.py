# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.database import Database
from openapi_server.models.database_collection import DatabaseCollection


pytestmark = pytest.mark.asyncio

async def test_databases_enumerate_databases(client):
    """Test case for databases_enumerate_databases

    Gets a list of databases in the migrate project.
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/databases'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_get_database(client):
    """Test case for databases_get_database

    Gets a database in the migrate project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/databases/{database_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

