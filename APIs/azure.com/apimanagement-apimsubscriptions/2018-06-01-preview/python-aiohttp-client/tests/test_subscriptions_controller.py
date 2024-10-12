# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscription_list_default_response import SubscriptionListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_subscription_regenerate_primary_key(client):
    """Test case for subscription_regenerate_primary_key

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/subscriptions/{sid}/regeneratePrimaryKey'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', sid='sid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_regenerate_secondary_key(client):
    """Test case for subscription_regenerate_secondary_key

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/subscriptions/{sid}/regenerateSecondaryKey'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', sid='sid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

