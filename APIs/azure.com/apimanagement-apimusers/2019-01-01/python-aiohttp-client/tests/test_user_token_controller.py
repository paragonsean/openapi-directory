# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_get_shared_access_token200_response import UserGetSharedAccessToken200Response
from openapi_server.models.user_get_shared_access_token_request import UserGetSharedAccessTokenRequest
from openapi_server.models.user_list_by_service_default_response import UserListByServiceDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_user_get_shared_access_token(client):
    """Test case for user_get_shared_access_token

    
    """
    parameters = openapi_server.UserGetSharedAccessTokenRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/users/{user_id}/token'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', user_id='user_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

