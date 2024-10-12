# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.managed_instance_operation_list_result import ManagedInstanceOperationListResult


pytestmark = pytest.mark.asyncio

async def test_managed_instance_operations_list_by_managed_instance(client):
    """Test case for managed_instance_operations_list_by_managed_instance

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}/operations'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

