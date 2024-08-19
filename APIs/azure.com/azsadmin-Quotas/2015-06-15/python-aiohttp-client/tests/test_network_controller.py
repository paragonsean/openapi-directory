# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.quota import Quota


pytestmark = pytest.mark.asyncio

async def test_quotas_create_or_update(client):
    """Test case for quotas_create_or_update

    
    """
    quota = {"properties":{"maxPublicIpsPerSubscription":1,"maxVnetsPerSubscription":7,"maxLoadBalancersPerSubscription":0,"maxVirtualNetworkGatewaysPerSubscription":2,"maxVirtualNetworkGatewayConnectionsPerSubscription":5,"migrationPhase":"None","maxNicsPerSubscription":6,"maxSecurityGroupsPerSubscription":5}}
    params = [('api-version', '2015-06-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network.Admin/locations/{location}/quotas/{resource_name}'.format(subscription_id='subscription_id_example', location='location_example', resource_name='resource_name_example'),
        headers=headers,
        json=quota,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quotas_delete(client):
    """Test case for quotas_delete

    
    """
    params = [('api-version', '2015-06-15')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network.Admin/locations/{location}/quotas/{resource_name}'.format(subscription_id='subscription_id_example', location='location_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

