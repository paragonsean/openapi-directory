# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.infra_role import InfraRole
from openapi_server.models.infra_role_list import InfraRoleList


pytestmark = pytest.mark.asyncio

async def test_infra_roles_get(client):
    """Test case for infra_roles_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoles/{infra_role}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', infra_role='infra_role_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_infra_roles_list(client):
    """Test case for infra_roles_list

    
    """
    params = [('api-version', '2016-05-01'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoles'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

