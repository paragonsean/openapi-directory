# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.management_policy import ManagementPolicy


pytestmark = pytest.mark.asyncio

async def test_management_policies_create_or_update(client):
    """Test case for management_policies_create_or_update

    
    """
    properties = {"properties":{"lastModifiedTime":"2000-01-23T04:56:07.000+00:00","policy":{"rules":[{"name":"name","definition":{"filters":{"blobTypes":["blobTypes","blobTypes"],"prefixMatch":["prefixMatch","prefixMatch"]},"actions":{"baseBlob":{"tierToArchive":{"daysAfterModificationGreaterThan":0.08008281904610115},"delete":{"daysAfterModificationGreaterThan":0.08008281904610115},"tierToCool":{"daysAfterModificationGreaterThan":0.08008281904610115}},"snapshot":{"delete":{"daysAfterCreationGreaterThan":0.6027456183070403}}}},"type":"Lifecycle","enabled":True},{"name":"name","definition":{"filters":{"blobTypes":["blobTypes","blobTypes"],"prefixMatch":["prefixMatch","prefixMatch"]},"actions":{"baseBlob":{"tierToArchive":{"daysAfterModificationGreaterThan":0.08008281904610115},"delete":{"daysAfterModificationGreaterThan":0.08008281904610115},"tierToCool":{"daysAfterModificationGreaterThan":0.08008281904610115}},"snapshot":{"delete":{"daysAfterCreationGreaterThan":0.6027456183070403}}}},"type":"Lifecycle","enabled":True}]}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/managementPolicies/{management_policy_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example', management_policy_name='management_policy_name_example'),
        headers=headers,
        json=properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_management_policies_delete(client):
    """Test case for management_policies_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/managementPolicies/{management_policy_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example', management_policy_name='management_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_management_policies_get(client):
    """Test case for management_policies_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/managementPolicies/{management_policy_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example', management_policy_name='management_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

