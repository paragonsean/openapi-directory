# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.restore_request_resource import RestoreRequestResource


pytestmark = pytest.mark.asyncio

async def test_restores_trigger(client):
    """Test case for restores_trigger

    
    """
    resource_restore_request = {"properties":{"objectType":"objectType"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/backupFabrics/{fabric_name}/protectionContainers/{container_name}/protectedItems/{protected_item_name}/recoveryPoints/{recovery_point_id}/restore'.format(vault_name='vault_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', container_name='container_name_example', protected_item_name='protected_item_name_example', recovery_point_id='recovery_point_id_example'),
        headers=headers,
        json=resource_restore_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

