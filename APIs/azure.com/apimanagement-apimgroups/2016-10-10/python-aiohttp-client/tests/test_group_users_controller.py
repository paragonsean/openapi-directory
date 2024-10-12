# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.group_users_list_by_groups200_response import GroupUsersListByGroups200Response
from openapi_server.models.groups_get_default_response import GroupsGetDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_group_users_create(client):
    """Test case for group_users_create

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/groups/{group_id}/users/{uid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', group_id='group_id_example', uid='uid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_users_delete(client):
    """Test case for group_users_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/groups/{group_id}/users/{uid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', group_id='group_id_example', uid='uid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_users_list_by_groups(client):
    """Test case for group_users_list_by_groups

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/groups/{group_id}/users'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', group_id='group_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

