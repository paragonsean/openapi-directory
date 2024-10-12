# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_get_identity_default_response import UserGetIdentityDefaultResponse
from openapi_server.models.user_group_list200_response import UserGroupList200Response


pytestmark = pytest.mark.asyncio

async def test_user_group_list(client):
    """Test case for user_group_list

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/users/{uid}/groups'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', uid='uid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

