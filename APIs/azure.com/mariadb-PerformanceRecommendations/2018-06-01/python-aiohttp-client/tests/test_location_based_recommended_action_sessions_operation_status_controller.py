# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.recommended_action_sessions_operation_status import RecommendedActionSessionsOperationStatus


pytestmark = pytest.mark.asyncio

async def test_location_based_recommended_action_sessions_operation_status_get(client):
    """Test case for location_based_recommended_action_sessions_operation_status_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DBforMariaDB/locations/{location_name}/recommendedActionSessionsAzureAsyncOperation/{operation_id}'.format(subscription_id='subscription_id_example', location_name='location_name_example', operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

