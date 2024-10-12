# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.performance_tier_list_result import PerformanceTierListResult


pytestmark = pytest.mark.asyncio

async def test_location_based_performance_tier_list(client):
    """Test case for location_based_performance_tier_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DBforPostgreSQL/locations/{location_name}/performanceTiers'.format(subscription_id='subscription_id_example', location_name='location_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

