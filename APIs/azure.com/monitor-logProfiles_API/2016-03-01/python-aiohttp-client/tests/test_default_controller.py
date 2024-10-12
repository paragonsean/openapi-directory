# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.log_profile_resource import LogProfileResource
from openapi_server.models.log_profile_resource_patch import LogProfileResourcePatch


pytestmark = pytest.mark.asyncio

async def test_log_profiles_update(client):
    """Test case for log_profiles_update

    
    """
    log_profiles_resource = {"properties":{"serviceBusRuleId":"serviceBusRuleId","storageAccountId":"storageAccountId","locations":["locations","locations"],"categories":["categories","categories"],"retentionPolicy":{"days":0,"enabled":True}},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/providers/microsoft.insights/logprofiles/{log_profile_name}'.format(subscription_id='subscription_id_example', log_profile_name='log_profile_name_example'),
        headers=headers,
        json=log_profiles_resource,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

