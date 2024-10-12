# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tenant_configuration_get_sync_state200_response import TenantConfigurationGetSyncState200Response


pytestmark = pytest.mark.asyncio

async def test_tenant_configuration_get_sync_state(client):
    """Test case for tenant_configuration_get_sync_state

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/tenant/{configuration_name}/syncState'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example', configuration_name='configuration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

