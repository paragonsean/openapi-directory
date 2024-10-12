# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authorize_request import AuthorizeRequest
from openapi_server.models.replication_status import ReplicationStatus


pytestmark = pytest.mark.asyncio

async def test_volumes_authorize_replication(client):
    """Test case for volumes_authorize_replication

    Authorize source volume replication
    """
    body = openapi_server.AuthorizeRequest()
    params = [('api-version', '2019-10-01')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}/volumes/{volume_name}/authorizeReplication'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example', volume_name='volume_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_break_replication(client):
    """Test case for volumes_break_replication

    Break volume replication
    """
    params = [('api-version', '2019-10-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}/volumes/{volume_name}/breakReplication'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example', volume_name='volume_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_delete_replication(client):
    """Test case for volumes_delete_replication

    Delete volume replication
    """
    params = [('api-version', '2019-10-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}/volumes/{volume_name}/deleteReplication'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example', volume_name='volume_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_replication_status(client):
    """Test case for volumes_replication_status

    Get volume replication status
    """
    params = [('api-version', '2019-10-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}/volumes/{volume_name}/replicationStatus'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example', volume_name='volume_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_resync_replication(client):
    """Test case for volumes_resync_replication

    Resync volume replication
    """
    params = [('api-version', '2019-10-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}/volumes/{volume_name}/resyncReplication'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example', volume_name='volume_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

