# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dedicated_host import DedicatedHost
from openapi_server.models.dedicated_host_update import DedicatedHostUpdate


pytestmark = pytest.mark.asyncio

async def test_dedicated_hosts_create_or_update(client):
    """Test case for dedicated_hosts_create_or_update

    
    """
    parameters = {"sku":{"tier":"tier","name":"name","capacity":1},"properties":{"licenseType":"None","instanceView":{"availableCapacity":{"allocatableVMs":[{"count":0.8008281904610115,"vmSize":"vmSize"},{"count":0.8008281904610115,"vmSize":"vmSize"}]},"assetId":"assetId","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}]},"provisioningTime":"2000-01-23T04:56:07.000+00:00","hostId":"hostId","provisioningState":"provisioningState","virtualMachines":[{"id":"id"},{"id":"id"}],"autoReplaceOnFailure":True,"platformFaultDomain":1}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/hostGroups/{host_group_name}/hosts/{host_name}'.format(resource_group_name='resource_group_name_example', host_group_name='host_group_name_example', host_name='host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_hosts_delete(client):
    """Test case for dedicated_hosts_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/hostGroups/{host_group_name}/hosts/{host_name}'.format(resource_group_name='resource_group_name_example', host_group_name='host_group_name_example', host_name='host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_hosts_get(client):
    """Test case for dedicated_hosts_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/hostGroups/{host_group_name}/hosts/{host_name}'.format(resource_group_name='resource_group_name_example', host_group_name='host_group_name_example', host_name='host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_hosts_update(client):
    """Test case for dedicated_hosts_update

    
    """
    parameters = {"properties":{"licenseType":"None","instanceView":{"availableCapacity":{"allocatableVMs":[{"count":0.8008281904610115,"vmSize":"vmSize"},{"count":0.8008281904610115,"vmSize":"vmSize"}]},"assetId":"assetId","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}]},"provisioningTime":"2000-01-23T04:56:07.000+00:00","hostId":"hostId","provisioningState":"provisioningState","virtualMachines":[{"id":"id"},{"id":"id"}],"autoReplaceOnFailure":True,"platformFaultDomain":1}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/hostGroups/{host_group_name}/hosts/{host_name}'.format(resource_group_name='resource_group_name_example', host_group_name='host_group_name_example', host_name='host_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

