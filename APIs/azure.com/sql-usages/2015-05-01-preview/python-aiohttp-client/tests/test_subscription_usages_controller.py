# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscription_usage import SubscriptionUsage
from openapi_server.models.subscription_usage_list_result import SubscriptionUsageListResult


pytestmark = pytest.mark.asyncio

async def test_subscription_usages_get(client):
    """Test case for subscription_usages_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Sql/locations/{location_name}/usages/{usage_name}'.format(location_name='location_name_example', usage_name='usage_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscription_usages_list_by_location(client):
    """Test case for subscription_usages_list_by_location

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Sql/locations/{location_name}/usages'.format(location_name='location_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

