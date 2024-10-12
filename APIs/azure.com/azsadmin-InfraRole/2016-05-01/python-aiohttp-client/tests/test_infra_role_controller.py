# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_infra_roles_restart(client):
    """Test case for infra_roles_restart

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoles/{infra_role}/Restart'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', infra_role='infra_role_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

