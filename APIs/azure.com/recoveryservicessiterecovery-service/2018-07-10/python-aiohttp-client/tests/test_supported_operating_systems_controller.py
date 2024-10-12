# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.supported_operating_systems import SupportedOperatingSystems


pytestmark = pytest.mark.asyncio

async def test_supported_operating_systems_get(client):
    """Test case for supported_operating_systems_get

    Gets the data of supported OSes by SRS.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationSupportedOperatingSystems'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

