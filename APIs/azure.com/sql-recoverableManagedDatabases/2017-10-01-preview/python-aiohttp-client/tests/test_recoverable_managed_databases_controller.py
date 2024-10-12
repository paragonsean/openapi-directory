# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.recoverable_managed_database import RecoverableManagedDatabase
from openapi_server.models.recoverable_managed_database_list_result import RecoverableManagedDatabaseListResult


pytestmark = pytest.mark.asyncio

async def test_recoverable_managed_databases_get(client):
    """Test case for recoverable_managed_databases_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}/recoverableDatabases/{recoverable_database_name}'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', recoverable_database_name='recoverable_database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recoverable_managed_databases_list_by_instance(client):
    """Test case for recoverable_managed_databases_list_by_instance

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}/recoverableDatabases'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

