# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cache import Cache
from openapi_server.models.caches_list_result import CachesListResult
from openapi_server.models.cloud_error import CloudError


pytestmark = pytest.mark.asyncio

async def test_caches_create_or_update(client):
    """Test case for caches_create_or_update

    
    """
    cache = {"name":"name","location":"location","id":"id","sku":{"name":"name"},"type":"type","properties":{"cacheSizeGB":0,"upgradeStatus":{"firmwareUpdateStatus":"available","firmwareUpdateDeadline":"2000-01-23T04:56:07.000+00:00","lastFirmwareUpdate":"2000-01-23T04:56:07.000+00:00","currentFirmwareVersion":"currentFirmwareVersion","pendingFirmwareVersion":"pendingFirmwareVersion"},"subnet":"subnet","mountAddresses":["mountAddresses","mountAddresses"],"health":{"statusDescription":"statusDescription","state":"Unknown"},"provisioningState":"Succeeded"},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StorageCache/caches/{cache_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', cache_name='cache_name_example'),
        headers=headers,
        json=cache,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_caches_delete(client):
    """Test case for caches_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StorageCache/caches/{cache_name}'.format(resource_group_name='resource_group_name_example', cache_name='cache_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_caches_flush(client):
    """Test case for caches_flush

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StorageCache/caches/{cache_name}/flush'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', cache_name='cache_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_caches_get(client):
    """Test case for caches_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StorageCache/caches/{cache_name}'.format(resource_group_name='resource_group_name_example', cache_name='cache_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_caches_list(client):
    """Test case for caches_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.StorageCache/caches'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_caches_list_by_resource_group(client):
    """Test case for caches_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StorageCache/caches'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_caches_start(client):
    """Test case for caches_start

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StorageCache/caches/{cache_name}/start'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', cache_name='cache_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_caches_stop(client):
    """Test case for caches_stop

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StorageCache/caches/{cache_name}/stop'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', cache_name='cache_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_caches_update(client):
    """Test case for caches_update

    
    """
    cache = {"name":"name","location":"location","id":"id","sku":{"name":"name"},"type":"type","properties":{"cacheSizeGB":0,"upgradeStatus":{"firmwareUpdateStatus":"available","firmwareUpdateDeadline":"2000-01-23T04:56:07.000+00:00","lastFirmwareUpdate":"2000-01-23T04:56:07.000+00:00","currentFirmwareVersion":"currentFirmwareVersion","pendingFirmwareVersion":"pendingFirmwareVersion"},"subnet":"subnet","mountAddresses":["mountAddresses","mountAddresses"],"health":{"statusDescription":"statusDescription","state":"Unknown"},"provisioningState":"Succeeded"},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StorageCache/caches/{cache_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', cache_name='cache_name_example'),
        headers=headers,
        json=cache,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_caches_upgrade_firmware(client):
    """Test case for caches_upgrade_firmware

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.StorageCache/caches/{cache_name}/upgrade'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', cache_name='cache_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

