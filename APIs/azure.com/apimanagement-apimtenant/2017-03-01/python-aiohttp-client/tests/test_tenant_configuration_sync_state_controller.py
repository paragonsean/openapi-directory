# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tenant_configuration_sync_state_contract import TenantConfigurationSyncStateContract


pytestmark = pytest.mark.asyncio

async def test_tenant_configuration_get_sync_state(client):
    """Test case for tenant_configuration_get_sync_state

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tenant/{configuration_name}/syncState'.format(configuration_name='configuration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

