# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.vault_usage_list import VaultUsageList


pytestmark = pytest.mark.asyncio

async def test_usages_list_by_vaults(client):
    """Test case for usages_list_by_vaults

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{vault_name}/usages'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vault_name='vault_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

