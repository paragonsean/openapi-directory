# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.preconfigured_endpoint_list import PreconfiguredEndpointList


pytestmark = pytest.mark.asyncio

async def test_preconfigured_endpoints_list(client):
    """Test case for preconfigured_endpoints_list

    Gets a list of Preconfigured Endpoints
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/NetworkExperimentProfiles/{profile_name}/PreconfiguredEndpoints'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', profile_name='profile_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

