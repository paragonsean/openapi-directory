# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_identity_collection import UserIdentityCollection
from openapi_server.models.users_list_by_service_default_response import UsersListByServiceDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_user_identities_list_by_users(client):
    """Test case for user_identities_list_by_users

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/users/{uid}/identities'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', uid='uid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

