# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_list_by_service_default_response import UserListByServiceDefaultResponse
from openapi_server.models.user_subscription_list200_response import UserSubscriptionList200Response


pytestmark = pytest.mark.asyncio

async def test_user_subscription_list(client):
    """Test case for user_subscription_list

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/users/{user_id}/subscriptions'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', user_id='user_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

