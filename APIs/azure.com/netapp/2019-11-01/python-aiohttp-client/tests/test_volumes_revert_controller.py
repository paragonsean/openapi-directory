# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.volume_revert import VolumeRevert


pytestmark = pytest.mark.asyncio

async def test_volumes_revert(client):
    """Test case for volumes_revert

    Revert a volume to one of its snapshots
    """
    body = openapi_server.VolumeRevert()
    params = [('api-version', '2019-11-01')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}/volumes/{volume_name}/revert'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example', volume_name='volume_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

