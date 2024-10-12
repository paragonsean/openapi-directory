# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.mount_target_list import MountTargetList


pytestmark = pytest.mark.asyncio

async def test_mount_targets_list(client):
    """Test case for mount_targets_list

    Describe all mount targets
    """
    params = [('api-version', '2019-08-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}/volumes/{volume_name}/mountTargets'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example', volume_name='volume_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

