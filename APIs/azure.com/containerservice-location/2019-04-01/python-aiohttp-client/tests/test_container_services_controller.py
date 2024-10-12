# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.orchestrator_version_profile_list_result import OrchestratorVersionProfileListResult


pytestmark = pytest.mark.asyncio

async def test_container_services_list_orchestrators(client):
    """Test case for container_services_list_orchestrators

    Gets a list of supported orchestrators in the specified subscription.
    """
    params = [('api-version', 'api_version_example'),
                    ('resource-type', 'resource_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ContainerService/locations/{location}/orchestrators'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

