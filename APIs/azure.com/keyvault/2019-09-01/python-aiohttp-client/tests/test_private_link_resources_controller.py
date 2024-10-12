# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.private_link_resource_list_result import PrivateLinkResourceListResult


pytestmark = pytest.mark.asyncio

async def test_private_link_resources_list_by_vault(client):
    """Test case for private_link_resources_list_by_vault

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.KeyVault/vaults/{vault_name}/privateLinkResources'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vault_name='vault_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

