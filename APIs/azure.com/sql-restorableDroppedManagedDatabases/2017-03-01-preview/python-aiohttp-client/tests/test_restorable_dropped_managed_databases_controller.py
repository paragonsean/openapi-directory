# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.restorable_dropped_managed_database import RestorableDroppedManagedDatabase
from openapi_server.models.restorable_dropped_managed_database_list_result import RestorableDroppedManagedDatabaseListResult


pytestmark = pytest.mark.asyncio

async def test_restorable_dropped_managed_databases_get(client):
    """Test case for restorable_dropped_managed_databases_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}/restorableDroppedDatabases/{restorable_dropped_database_id}'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', restorable_dropped_database_id='restorable_dropped_database_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restorable_dropped_managed_databases_list_by_instance(client):
    """Test case for restorable_dropped_managed_databases_list_by_instance

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}/restorableDroppedDatabases'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

