# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.machine import Machine
from openapi_server.models.machine_collection import MachineCollection


pytestmark = pytest.mark.asyncio

async def test_machines_enumerate_machines(client):
    """Test case for machines_enumerate_machines

    Gets a list of machines in the migrate project.
    """
    params = [('api-version', 'api_version_example'),
                    ('continuationToken', 'continuation_token_example'),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/machines'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_machines_get_machine(client):
    """Test case for machines_get_machine

    Gets a machine in the migrate project.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Migrate/migrateProjects/{migrate_project_name}/machines/{machine_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', migrate_project_name='migrate_project_name_example', machine_name='machine_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

