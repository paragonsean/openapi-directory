# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.file_share import FileShare
from openapi_server.models.file_share_items import FileShareItems


pytestmark = pytest.mark.asyncio

async def test_file_shares_create(client):
    """Test case for file_shares_create

    
    """
    file_share = {"properties":{"shareQuota":410,"metadata":{"key":"metadata"},"lastModifiedTime":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/fileServices/default/shares/{share_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=file_share,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_shares_delete(client):
    """Test case for file_shares_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/fileServices/default/shares/{share_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_shares_get(client):
    """Test case for file_shares_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/fileServices/default/shares/{share_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_shares_list(client):
    """Test case for file_shares_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example'),
                    ('$maxpagesize', 'maxpagesize_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/fileServices/default/shares'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_shares_update(client):
    """Test case for file_shares_update

    
    """
    file_share = {"properties":{"shareQuota":410,"metadata":{"key":"metadata"},"lastModifiedTime":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/fileServices/default/shares/{share_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', share_name='share_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=file_share,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

