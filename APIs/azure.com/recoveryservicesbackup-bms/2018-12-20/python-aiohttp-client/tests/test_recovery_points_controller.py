# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.crr_access_token_resource import CrrAccessTokenResource


pytestmark = pytest.mark.asyncio

async def test_recovery_points_get_access_token(client):
    """Test case for recovery_points_get_access_token

    Returns the Access token for communication between BMS and Protection service
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/backupFabrics/{fabric_name}/protectionContainers/{container_name}/protectedItems/{protected_item_name}/recoveryPoints/{recovery_point_id}/accessToken'.format(vault_name='vault_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', container_name='container_name_example', protected_item_name='protected_item_name_example', recovery_point_id='recovery_point_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

