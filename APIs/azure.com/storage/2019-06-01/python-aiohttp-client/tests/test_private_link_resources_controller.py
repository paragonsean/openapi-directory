# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.private_link_resource_list_result import PrivateLinkResourceListResult


pytestmark = pytest.mark.asyncio

async def test_private_link_resources_list_by_storage_account(client):
    """Test case for private_link_resources_list_by_storage_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/privateLinkResources'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

