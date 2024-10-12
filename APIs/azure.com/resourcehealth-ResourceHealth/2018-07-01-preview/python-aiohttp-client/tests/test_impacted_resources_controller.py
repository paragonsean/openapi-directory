# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.impacted_resource_list_result import ImpactedResourceListResult


pytestmark = pytest.mark.asyncio

async def test_impacted_resources_list_by_subscription_id(client):
    """Test case for impacted_resources_list_by_subscription_id

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ResourceHealth/impactedResources'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

